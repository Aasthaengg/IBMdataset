N,K,S = list(map(int,input().split()))
if S == 10**9:
    n = 1
else:
    n = 10**9
L = [S]*K+[n]*(N-K)
print(*L)