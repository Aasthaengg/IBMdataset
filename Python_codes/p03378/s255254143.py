n,m,x = map(int,input().split())
a = list(map(int,input().split()))
map = [0]*(n+1)
for i in range(m):
	map[a[i]] += 1
ans_l = map[1:x]
ans_r = map[x+1:n]
ans = min(sum(ans_l),sum(ans_r))
print(ans)