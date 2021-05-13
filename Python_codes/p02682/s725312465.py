a, b, c, k = map(int, input().split())

import sys

ans = 0
if a != 0 and a >= k:
    # a = 1
    print(k)
    sys.exit()
elif a != 0:
    ans += a
    k -= a

if b != 0 and b >= k:
    print(ans)
    sys.exit()
elif b != 0:
    k -= b

ans += k * -1
print(ans)
