N,X=map(int,input().split())
m = []

for _ in range(N):
	m.append(int(input()))

print(N+(X-sum(m))//min(m))

