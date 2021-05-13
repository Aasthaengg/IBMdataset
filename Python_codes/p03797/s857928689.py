N, M = map(int, input().split())
cnt = 0

if N<=M//2:
    cnt = N
    N,M =0,M-2*N
    cnt += M//4
    print(cnt)
else:
    cnt = M//2
    print(cnt)