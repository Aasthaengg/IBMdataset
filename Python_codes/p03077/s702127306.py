import math
n = int(input())
transportation = [int(input()) for i in range(5)]
bottleneck = min(transportation)
ans = 0
if bottleneck >= n:
	ans = 5
else:
	ans = math.ceil((n-bottleneck)/bottleneck)+5
print(ans)
