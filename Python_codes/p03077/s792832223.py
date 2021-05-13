import math
n = int(input())
Min = 10000000000000000
for _ in range(5):
	Min = min(int(input()),Min)

ans = 4
ans += math.ceil(n/Min)
print(ans)
