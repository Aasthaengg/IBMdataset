N, K = map(int, input().split())
p = list(map(int, input().split()))
	
p.sort()
count = 0
for num in range(K):
	count += p[num]

print(count)