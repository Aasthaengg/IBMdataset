import sys
sys.setrecursionlimit(10**9)

N,M=map(int,input().split())
graph=[[] for _ in range(N)]

for _ in range(M):
  l,r,d=map(int,input().split())
  l,r=l-1,r-1
  graph[l].append([r,d])
  graph[r].append([l,-d])

def BFD(x):
  global checked,answer,graph
  checked[x]=1
  for i,distance in graph[x]:
    if answer[i]=="first":
      answer[i]=answer[x]+distance
    else:
      if answer[i]!=answer[x]+distance:
        print("No")
        exit()
    
    if checked[i]==0:
      BFD(i)

checked=[0]*N
answer=["first"]*N

for i in range(N):
  if checked[i]==0:
    answer[i]=0
    BFD(i)

print("Yes")