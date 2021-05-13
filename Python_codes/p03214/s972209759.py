N = int(input())
a = list(map(int,input().split()))
avg = 0
for i in range(N):
	avg+=a[i]
avg=avg/len(a)
min = 100
ans = 0
for i in range(N):
	if min > abs(avg - a[i]):
		ans = i
		min = abs(avg - a[i])
print(ans)