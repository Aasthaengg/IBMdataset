import copy
n = int(input())
t = list(map(int,input().split()))
m = int(input())
tmp = list(t)
for i in range(m):
  p,x = map(int,input().split())
  p = p-1
  tmp[p] = x
  print(sum(tmp))
  tmp[p] = t[p]