n = int(input())
a = list(map(int,input().split()))
answer = 0 
m = a[0]

for i in range(1,n):
	m *= a[i]

for i in range(n):
	answer += (m-1) % a[i]

print(answer) 