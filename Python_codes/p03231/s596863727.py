from collections import defaultdict
from fractions import gcd
N, M = map(int, input().split())
S = input()
T = input()
L = N * M // gcd(N, M)
ds = L // N
dt = L // M
dict_s = defaultdict(str)
dict_t = defaultdict(str)

for i in range(N):
  dict_s[i*ds] = S[i]
  
for i in range(M):
  dict_t[i*dt] = T[i]

for key in dict_s.keys():
  if key in dict_t.keys():
    if dict_s[key] != dict_t[key]:
      print(-1)
      exit()
print(L)