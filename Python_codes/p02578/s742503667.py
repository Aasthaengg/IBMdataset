n = int(input())
a = list(map(int,input().split()))
ans,check = 0,a[0]
for i in range(1,n):
	if check > a[i]:
		ans += check - a[i]
	else:
		check = a[i]
print(ans)
