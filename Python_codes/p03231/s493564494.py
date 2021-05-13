import fractions
N, M = list(map(int, input().split()))
S = input()
T = input()
d = fractions.gcd(N,M)
n = N//d
m = M//d
for i in range(d):
    if S[i*n] != T[i*m]:
        flag = False
        break
    else:
        flag = True
if flag:
  print((N*M)//d)
else:
  print(-1)