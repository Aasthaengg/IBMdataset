from fractions import gcd

N, M = map(int,input().split())
S = list(input())
T = list(input())

gc = gcd(N, M)

ans = N*M//gc

for i in range(gc):
    if S[N//gc*i] != T[M//gc*i]:
        ans = -1
        break
                
print(ans)