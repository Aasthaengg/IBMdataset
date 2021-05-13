n = int(input())
a = list(map(int,input().split()))
ans,box= 0,[]
sum = sum(a)
for i in range(n-1):
	ans += a[i]
	sum -= a[i]
	box.append(abs(ans-sum))
print(min(box))