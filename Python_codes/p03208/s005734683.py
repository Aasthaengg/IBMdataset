n,k = map(int,input().split())
h = [0]*n
for i in range(n):
	h[i] = int(input())
h.sort()
min = pow(10,9)
for i in range(n+1-k):
	m = h[i+k-1]-h[i]
	if m < min:
		min = m
print(min)