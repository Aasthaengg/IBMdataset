N, K = map(int, input().split())

if K % 2 == 1:
    print((N//K)**3)
else:
    if N % K >= K/2:
        add = 1
    else:
        add = 0
    print(((N//K+add)**3 + (N//K)**3))
