n = int(input())

cnt = 0
a = list(map(int, input().split()))
for i in range(n):
	x = a[i]
	if(i%2==0 and x%2==1):
		cnt += 1
print(cnt)
