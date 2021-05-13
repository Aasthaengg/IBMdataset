N = int(input())

XY = []
for _ in range(N):
    A = int(input())

    temp = []
    for _ in range(A):
        temp.append(list(map(int, input().split())))

    XY.append(temp)


max_honest = 0
for c in range(1 << N):
    check = [0] * N
    contradict = False
    temp = c

    cnt2 = 0
    while temp != 0:
        if 1 & temp:
            check[cnt2] = 1

        temp >>= 1
        cnt2 += 1

    for i in range(N):
        if check[i] == 1:
            for x, y in XY[i]:
                if check[x - 1] != y:
                    contradict = True
                    break

            if contradict:
                break

    if not contradict:
        cnt1 = 0
        for i in range(N):
            if check[i] is not None and check[i] == 1:
                cnt1 += 1

        max_honest = max(max_honest, cnt1)


print(max_honest)
