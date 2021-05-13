from math import inf

n = int(input())
h = list(map(int, input().split()))

costs = [inf]*n
costs[0] = 0

for i in range(n):
	for j in (i+1, i+2):
		if j < n:
			costs[j] = min(costs[j], costs[i]+abs(h[i]-h[j]))
print(costs[-1])