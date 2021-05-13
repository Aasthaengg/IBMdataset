import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N,M = map(int,input().split())
lst=[{} for f in range(N)]
for i in range(M):
 x,y=map(int,input().split())
 lst[x-1][y-1]=1
memo = {}
def cost(a):
 ans=0
 for i in lst[a]: 
  if i in memo:
    ans=max(memo[i]+1,ans)
  else:
    ans=max(cost(i)+1,ans)
 memo[a]=ans
 return ans
T=0
for i in range(N):
 T=max(T,cost(i))
print(T)