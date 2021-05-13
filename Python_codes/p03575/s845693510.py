from collections import defaultdict
vis = [0 for i in range(0 , 2000)]
lt = [0 for i in range(0 , 2000)]
dis = [0 for i in range(0 , 2000)]
adj = defaultdict(list)
time = 0
ans = 0
def dfs(u , p):
	global time , ans
	time = time+1
	lt[u]= dis[u]=time
	vis[u]=1
	for v in adj[u]:
		if v==p:
			continue
		if vis[v]==0:
			dfs(v , u)
			lt[u]=min(lt[u] , lt[v])# if back edge through child v
			if lt[v]>dis[u]:
				ans = ans+1
		else:
			lt[u]=min(lt[u] , dis[v])# if there is a back edge to a child v
def main():
	n , m = map(int , input().split())
	for i in range(0 , m):
		u, v= map(int , input().split())
		adj[u].append((v))
		adj[v].append((u))
	dfs(1, 0)
	print(ans)
if __name__=="__main__":
	main()