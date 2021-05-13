import sys
input = sys.stdin.readline
from collections import defaultdict

N,K = list(map(int,input().split()))
data = [list(map(int, input().split())) for _ in range(N)]

data.sort(key=lambda x:-x[1])
KISO = 0
EAT = defaultdict(int)
for i in range(K):
  t,v = data[i]
  EAT[t] += 1
  KISO += v
SHURUI = len(EAT)
l = K-1
r = K
MAX = KISO+SHURUI**2
while True:
  if l<0 or r>=N: break
  a,b = data[l]
  c,d = data[r]
  if EAT[a] == 1:
    l -= 1
    continue
  if EAT[c] != 0:
    r += 1
    continue
  EAT[a] -= 1
  EAT[c] += 1
  KISO -= b
  KISO += d
  SHURUI += 1
  l -= 1
  r += 1
  MAX = max(MAX,KISO+SHURUI**2)
print(MAX)