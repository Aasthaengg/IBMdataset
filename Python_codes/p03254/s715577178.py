def resolve():
    N, x = [int(i) for i in input().split()]
    A = sorted([int(i) for i in input().split()])
    sumA = 0
    cnt = 0
    for i in range(N):
        if A[i] <= (x - sumA):
            sumA += A[i]
            cnt += 1
        else:
            break
    else:
        if sumA != x:
            cnt -= 1
    print(cnt)


resolve()
