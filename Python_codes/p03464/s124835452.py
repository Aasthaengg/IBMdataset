K = int(input())
A = list(map(int, input().split()))

if A[-1] != 2:
    print(-1)
    exit()
else:
    m, M = 2, 3
    for i in range(K-2, -1, -1):
        if A[i] > M:
            print(-1)
            exit()
        else:
            if m % A[i] != 0:
                m = (m // A[i] + 1) * A[i]
            M = (M // A[i] + 1) * A[i] - 1
if m > M:
    print(-1)
    exit()
else:
    print(m, M)