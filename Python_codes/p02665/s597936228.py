import sys
from functools import lru_cache
 
#read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10**6)
def read():
  return int(readline())
def reads():
  return map(int, readline().split())
def mp(arg):
  return map(int,arg.split())

n=read()
a=list(reads())
if a[0]>1:
  print("-1")
  exit()
res=0
node=[0 for _ in range(n+1)]
node[-1]=a[-1]
#node[-1][0]=node[-1][1]=a[-1]
#sub=[0]*n
for i in range(n-1,-1,-1):
  #node[i][0]=(node[i+1][0]+1)//2+a[i]
  node[i]=min(node[i+1]+a[i],1<<i)
#print(node)
for i in range(n):
  sub=node[i]-a[i]
  node[i+1]=min(node[i+1],sub*2)
#print(sub)
#print(node)
for i in range(n+1):
  if node[i]<a[i]:
    print("-1")
    exit()
  if (node[i]<=0 and i<n) :
    print("-1")
    exit()
  res+=node[i]
print(res)
