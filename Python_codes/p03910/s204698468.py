import sys, math, itertools, collections, bisect
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8')
inf = float('inf') ;mod = 10**9+7
mans = inf ;ans = 0 ;count = 0 ;pro = 1
ans = []
n = int(input())
for i in range(n+1):
  s = i*(i+1)//2
  if s >= n:
    k = i
    break
sabun = s - n
for i in range(k,0,-1):
  # print(sabun)
  if sabun >= i:
    sabun -= i
  else:
    ans.append(i)
print(*reversed(ans),sep = "\n")
# print(k)