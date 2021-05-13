N,T = map(int,input().split())
ans = T
switch = list(map(int,input().split()))
for i in range(1,N):
	if switch[i] - switch[i - 1] < T:
		ans += switch[i] - switch[i - 1]
	else:
		ans += T
print(ans)