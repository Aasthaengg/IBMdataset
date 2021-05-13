n = int(input())
d,x = map(int,input().split())
a = [int(input()) for i in range(n)]

cnt = 0
day = 1
for i in range(n):
	while day <= d:
		day += a[i]
		cnt += 1
	x += cnt
	cnt = 0
	day = 1

print(x)