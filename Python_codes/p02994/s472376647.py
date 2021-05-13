N, L = map(int, input().split())
if L < 0:
    if N <= (-L):
        print(sum([i for i in range(L, L + N - 1)]))
    else:
        print(sum([i + L for i in range(N)]))
else:
    print(sum([i for i in range(L + 1, N + L)]))
