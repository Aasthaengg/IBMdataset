from collections import deque
from sys import stdin
input=stdin.readline

N=int(input())
a=[0]*(N-1)
b=[0]*(N-1)
c=[0]*(N-1)
L=[ [] for _ in range(N)]
for i in range(N-1):
  a[i],b[i],c[i]= map(int,input().split())
  L[a[i]-1].append((b[i]-1,c[i]))
  L[b[i]-1].append((a[i]-1,c[i]))
Q,K= map(int,input().split())
         
#Lの中のitemの0は接続先、1は距離

d=[ -1 for i in range(N)]

def BFS(x):
  v=deque([x])
  d[x]=0
  
  while len(v)>0:
    s=v.popleft() #sはint
    for item in L[s]:
      if d[item[0]]==-1:
        d[item[0]]=d[s]+item[1]
        v.append(item[0])
BFS(K-1)

x=[0]*Q
y=[0]*Q
for i in range(Q):
  x[i],y[i] = map(int,input().split())
  print(d[x[i]-1]+d[y[i]-1])