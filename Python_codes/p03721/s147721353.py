n,k = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
a.sort(key=lambda x:x[0])
ans,i = 0,0
t = 0
while(ans < k):
	ans += a[i][1]
	t = a[i][0]
	i += 1
print(t)