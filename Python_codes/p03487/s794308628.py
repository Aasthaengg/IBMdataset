from collections import *
N = int(input())
C = Counter(list(map(int,input().split())))
ans = 0

for k,v in C.items():
  if k<v:
    ans+=v-k
  elif v<k:
    ans+=v

print(ans)