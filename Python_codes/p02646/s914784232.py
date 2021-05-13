import sys, math, itertools, collections, bisect
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8')
inf = float('inf') ;mod = 10**9+7
mans = inf ;ans = 0 ;count = 0 ;pro = 1

a,v=map(int,input().split())
b,w = map(int,input().split())
V  = v-w
t = int(input())
d = abs(a-b)
if V <= 0:
  if d == 0:print("YES")
  else:
    print("NO")
  exit()
def ceil(x,y):
  return (x-1)//y+1
if ceil(d,V) <= t:
  print("YES")
else:
  print("NO")