n = int(input())
a = list(map(int, input().split()))
cnt=[0]*n
for i in range(n):
	while a[i]%2==0:
		a[i]//=2
		cnt[i]+=1
print(min(cnt))