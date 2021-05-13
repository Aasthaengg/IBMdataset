import sys
from collections import deque
input = sys.stdin.readline
n=int(input())
l=[[] for i in range(n)]
for i in range(n-1):
  a,b,c=map(int,input().split())
  l[a-1].append([b-1,c])
  l[b-1].append([a-1,c])
ans=[-1]*n
q,k=map(int,input().split())
ans[k-1]=0
d=deque([k-1])
while d:
  now=d.pop()
  for x in l[now]:
    a,b=x
    if ans[a]<0:
      ans[a]=ans[now]+b
      d.appendleft(a)
for i in range(q):
  a,b=map(int,input().split())
  print(ans[a-1]+ans[b-1])