N, M = map(int, input().split())
S = str(input())
T = str(input())

from fractions import gcd
L = N * M // gcd(N, M)
step_s = L // M
step_t = L // N
stop = N // step_s
flag = True

for i in range(stop):
  #print(i, S[i * step_s], T[i * step_t])
  if S[i * step_s] != T[i * step_t]:
    flag = False
    break

if flag:
  print(L)
else:
  print(-1)