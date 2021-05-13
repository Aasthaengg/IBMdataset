import math
a,b = list(map(int, input().split()))
ans = 1
b -= a
ans += math.ceil(b / (a-1))
print(ans)
