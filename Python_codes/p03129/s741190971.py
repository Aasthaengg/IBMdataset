import math

n, k = map(int, input().split())
print("YES" if math.ceil(n / 2) >= k else "NO")