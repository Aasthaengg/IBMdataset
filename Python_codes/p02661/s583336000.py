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
a,b=[0]*n,[0]*n
for i in range(n):
  a[i],b[i]=reads()
a=sorted(a)
b=sorted(b)
if n%2==1:
  print(b[(n-1)//2]-a[(n-1)//2]+1)
else:
  mi=(a[n//2-1],a[n//2])
  ma=(b[n//2-1],b[n//2])
  res=(ma[0]+ma[1])-(mi[0]+mi[1])+1
  print(res)