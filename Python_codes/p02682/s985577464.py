import sys
input = sys.stdin.readline

a, b, c, k = map(int, input().split())
if a >= k: print(k)
else:
    # Continue
    res = a
    k -= a
    if b >= k: print(res)
    else:
        # Continue
        k -= b
        print(res - k)