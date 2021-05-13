import sys
import math

n, k = map(int, input().split())
a = list(map(int, input().split()))


def ok(x):
    b = []
    for an in a:
        b.append(an % x)
    b.sort(reverse=True)
    print(x, a, b, file=sys.stderr)
    t = int(sum(b) / x)
    print(t, sum(b[t:]), file=sys.stderr)
    if t == 0:
        return True
    return True if sum(b[t:]) <= k else False


s = 0
for an in a:
    s += an

ans = 1
for x in range(1, int(math.sqrt(s)) + 1):
    if s % x != 0:
        continue
    if ok(x):
        ans = max(ans, x)
    if ok(int(s / x)):
        ans = max(ans, int(s / x))

print(ans)
