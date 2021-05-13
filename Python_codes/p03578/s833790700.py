from collections import *
n=int(input())
d=list(map(int,input().split()))
dc=Counter(d)
m=int(input())
t=list(map(int,input().split()))
tc=Counter(t)
s=set(d)|set(t)
for i in s:
  if dc[i]<tc[i]:
    print('NO')
    exit()
print('YES')