import sys
sys.setrecursionlimit(10**5+1)

N,M = map(int,input().split())
nodes = [[] for _ in range(N)]

for _ in range(M):
  x,y = map(int,input().split())
  nodes[x-1].append(y-1)
  
dp = [-1]*N

def judge(index):
  if dp[index] != -1:
    return dp[index]
  else:
    edges = 0
    for i in nodes[index]:
      edges = max(edges, 1+judge(i))
    dp[index] = edges
    return edges

answer = 0
for i in range(N):
  answer = max(answer, judge(i))
print(answer)