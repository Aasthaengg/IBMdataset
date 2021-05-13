N,M = [int(i) for i in input().split()]
S = 0

if N <= M//2:
    S = N + (M - 2*N)//4
else:
    if N > M//2:
        S = M//2
    else:
        S = N

print(S)
