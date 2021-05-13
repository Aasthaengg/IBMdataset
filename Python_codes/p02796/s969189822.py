import sys
input = sys.stdin.readline
n = int(input())
c = []
for i in range(n):
  l,x = map(int,input().split())
  c.append((l-x,l+x))
  
from operator import itemgetter
c = sorted(c,key=itemgetter(0))
c = sorted(c,key=itemgetter(1))

ans = 1
chk = c[0][1]
for i,j in c:
  if i >= chk:
    ans +=1
    chk = j
    
print(ans)