from collections import *
N = int(input())
C = Counter([int(input()) for n in range(N)])
ans = 0

for v in C.values():
  if v%2==1:
    ans+=1

print(ans)