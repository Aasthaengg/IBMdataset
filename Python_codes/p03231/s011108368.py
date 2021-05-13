import math
N,M = map(int, input().split())
S = input()
T = input()

if S[0] != T[0]:
  print(-1)
  exit()

lcm = N * M // math.gcd(N, M)
#1,(L/N) +1, 2*(L/N) +1..(N-1)*(L/N)+1
tekito =[]
for i in range(1,N):
  tekito.append(i*(lcm//N)+1)
tekitu =[]
for i in range(1,M):
  tekitu.append(i*(lcm//M)+1)

gattai = set(tekito) & set(tekitu) 
for k in gattai:
  i1 = (k-1) // (lcm//N)
  i2 = (k-1) // (lcm//M)
  if S[i1] != T[i2]:
    print(-1)
    exit()
print(lcm)
