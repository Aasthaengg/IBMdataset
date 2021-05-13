# distance between two nodes is dis(root, a)+dis(root, b)-2*(dis(lca(a,b),root))
# taking mod 2 last term is eliminated 
# all nodes having dis as odd parity from root will be white color
# all nodes having dis as even parity from root will be even color
import sys
import os
sys.setrecursionlimit(1000000)
from collections import defaultdict
adj = defaultdict(list)
dis =[0 for i in range(1000000)]
def dfs(u , p):
	for i , w in adj[u]:
		if i==p:
			continue
		dis[i]=dis[u]+w
		dis[i]=dis[i]%2
		dfs(i , u)
def main():
	n = int(input())
	for i in range(n-1):
		x, y , w = map(int , input().split())
		w = w%2
		adj[x].append([y , w])
		adj[y].append([x, w])
	dfs(1, 0)
	for i in range(1,n+1):
		print(dis[i])
if __name__ =="__main__":
	main()