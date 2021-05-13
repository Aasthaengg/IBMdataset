import math
n, k = map(int, input().split())

if round(n / 2) >= k or (n == 1 and k == 1):
    print("YES")
else:
    print("NO")
