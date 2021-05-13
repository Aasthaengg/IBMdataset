def mi(): return map(int,input().split())
def lmi(): return list(map(int,input().split()))
def ii(): return int(input())
def isp(): return input().split()
from collections import deque
n,m=mi()
adjacent_list=[[] for i in range(n+1)]
for i in range(m):
  a,b=mi()
  adjacent_list[a].append(b)
  adjacent_list[b].append(a)
#print(adjacent_list)

dp=[0]*(n+1)

que=deque()
que.append(1)
while que:
  p=que.popleft()
  for i in adjacent_list[p]:
    if dp[i]==0:
      dp[i]=p
      que.append(i)
      
print('Yes')
for i in range(2,n+1):
  print(dp[i])