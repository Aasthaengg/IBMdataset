from collections import deque
import sys
input=sys.stdin.readline
n=int(input())
a=[deque(list(map(int,input().split()))) for _ in range(n)]
def find(cand):
  s=set()
  for i in cand:
    if a[i] and a[a[i][0]-1]:
      if i==a[a[i][0]-1][0]-1:
        s.add(i)
        s.add(a[i][0]-1)
  for i in s:
    a[i].popleft()
  return len(s),s
cand=set(range(n))
game=n*(n-1)//2
ans=0
while 1:
  num,cand=find(cand)
  if num==0:
    print(-1)
    break
  ans+=1
  game-=num//2
  if game==0:
    print(ans)
    break