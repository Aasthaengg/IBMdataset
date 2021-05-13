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

    cnt1 = 0
    while c != 0:
        if 1 & c:
            check[cnt1] = 1

        c >>= 1
        cnt1 += 1

    for i in range(N):
        if check[i] == 1:
            for x, y in XY[i]:
                if check[x - 1] != y:
                    contradict = True
                    break

            if contradict:
                break

    if not contradict:
        max_honest = max(max_honest, sum(check))


print(max_honest)
