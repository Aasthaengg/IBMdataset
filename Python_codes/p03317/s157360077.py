import math
n, k = map(int, input().split())
a = list(map(int, input().split()))
ans = n - k
c = 0
if ans > 0:
    c = math.ceil(ans / (k-1))

print(c+1)