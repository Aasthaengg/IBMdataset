n = int(input())
b = list(map(int,input().split()))
"""
b_i >= max(a_i, a_(i+1))
"""
a = [10**18 for _ in range(n)]
for i in range(n):
	if i == 0:
		a[i] = b[i]
	elif i == n-1:
		a[i] = b[i-1]
	else:
		a[i] = min(b[i], b[i-1])
print(sum(a))