N,M = map(int, open(0).read().split())
if 2 * N > M:
    print(M//2)
else:
    rem = M - 2 * N
    print(N+rem//4)