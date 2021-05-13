import math

def makelist(n, m):
    return [[0 for _ in range(m)] for _ in range(n)]


W, a, b = list(map(int, input().split()))
if b <= a <= b+W or b <= a+W <= b+W:
    print(0)
else:
    ans = min(abs(b+W-a), abs(a+W-b))
    print(ans)
