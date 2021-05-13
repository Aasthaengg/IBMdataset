n = int(input())
route = [[] for i in range(n)] #どの木と隣接か
for i in range(n-1):
	a,b = (x-1 for x in map(int,input().split()))
	route[a]+=[b]
	route[b]+=[a]
c = list(map(int,input().split()))
c.sort(reverse=1)

check = [False]*n #check済みか否か
ans = [0]*n #cを入れてく
cnt = 0 #何個目を見てるか、cに使う
q = [0]
# print(route)
while q:
	cur = q[0] #今どこの木を見てるか
	q = q[1:]
	check[cur] = True
	ans[cur] = c[cnt]
	cnt += 1
	for r in route[cur]:
		if check[r]:
			continue
		q.append(r)
print(sum(ans[1:]))
print(*ans)