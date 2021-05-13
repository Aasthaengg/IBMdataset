answer = 0
n,m,c = map(int,input().split())
b = list(map(int,input().split()))

for i in range(n):
	result = c
	a = list(map(int,input().split()))
	for j in range(m):
		result += a[j] * b[j]
	if result > 0:
		answer += 1

print(answer)