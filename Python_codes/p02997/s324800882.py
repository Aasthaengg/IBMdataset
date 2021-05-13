def connect(n,k,ans,edge_list):
	for u in range(1,n):
		for v in range(u+1,n):
			if k==ans:
				return
			else:
				edge_list.append((u,v))
				ans -= 1

def solve(n,k):
	edge_list = []
	ans = 0

	for u in range(1,n):
		ans += len(edge_list)
		edge_list.append((u,n))

	if k > ans:
		print(-1)
		return

	connect(n,k,ans,edge_list)
	print(len(edge_list))
	for edge in edge_list:
		print(*edge)

solve(*map(int,input().split()))