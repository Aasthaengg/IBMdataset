import numpy as np
n = int(input())
a = list(map(int, input().split()))
m = np.mean(a)
ans = 0
mx = 999999
for i in range(n):
	if abs(a[i] - m) < mx:
		mx = abs(a[i] - m)
		ans = i
print(ans)
