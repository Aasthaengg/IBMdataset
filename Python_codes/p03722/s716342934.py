import sys
input=sys.stdin.readline
n,m=map(int,input().split())
graph=[]
for _ in range(m):
    a,b,c=map(int,input().split())
    graph.append([a-1,b-1,-c])

def BellmanFord(n,m,graph):
    costs=[float("inf")]*n
    costs[0]=0
    for _ in range(n-1):
        for i in range(m):
            if costs[graph[i][1]]>costs[graph[i][0]]+graph[i][2]:
                costs[graph[i][1]]=costs[graph[i][0]]+graph[i][2]
    newcosts=[]
    for i in costs:
        newcosts.append(i)
    for _ in range(n):
        for i in range(m):
            if newcosts[graph[i][1]]>newcosts[graph[i][0]]+graph[i][2]:
                newcosts[graph[i][1]]=newcosts[graph[i][0]]+graph[i][2]
    if newcosts[n-1]!=costs[n-1]:
        return "inf"
    else:
        return -costs[n-1]

print(BellmanFord(n,m,graph))