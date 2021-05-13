import sys
N = int(input())
g = [[] for _ in range(N + 5)]
Fennec = [0]*(N+10)
Sunuke = [0]*(N+10)
sys.setrecursionlimit(10**8)

def dfs(r,f,d,dist):
	dist[r]=d
	for x in range(len(g[r])):
		if g[r][x]==f : continue
		else : dfs(g[r][x],r,d+1,dist)

# main

for i in range(N-1):
	a,b=map(int,input().split())
	a-=1
	b-=1
	g[a].append(b)
	g[b].append(a)
dfs(0,-1,0,Fennec)
dfs(N-1,-1,0,Sunuke)
ans = int(0)

for i in range(N):
	if Fennec[i]<=Sunuke[i] : ans+=1
	else : ans-=1
if(ans>0):
	print("Fennec")
else:
	print("Snuke")
