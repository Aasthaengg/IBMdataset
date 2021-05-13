import math

N, K = map(int, input().split())
print("YES" if K <= math.ceil(N/2) else "NO")