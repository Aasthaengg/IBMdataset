n,k = map(int,input().split())
h = [int(input()) for _ in range(n)]
h.sort()
a = h[n-1] + 1
for i in range(n-k+1):
	if h[i+k-1] - h[i] < a:
		a = h[i+k-1] - h[i]
print(a)