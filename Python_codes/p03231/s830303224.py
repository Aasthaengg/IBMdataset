import math
 
N,M = map(int,input().split())
S = list(str(input()))
T = list(str(input()))
g = math.gcd(N,M)
gn,gm = N//g,M//g
for i in range(g):
  if S[i*gn] != T[i*gm]:
    print(-1)
    exit()

print(gn*gm*g)