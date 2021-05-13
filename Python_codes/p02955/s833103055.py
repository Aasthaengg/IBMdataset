import sys
import math

n, k = map(int, input().split())
a = list(map(int, input().split()))


def ok(x):
    b = [i % x for i in a]
    b.sort(reverse=True)
    t = int(sum(b) / x)
    if t == 0:
        return True
    return True if sum(b[t:]) <= k else False


s = sum(a)
sqs = int(math.sqrt(s))
ans = 1
for x in range(1, sqs + 1):
    if s % x != 0:
        continue
    if ok(x):
        ans = max(ans, x)
    if ok(int(s / x)):
        ans = max(ans, int(s / x))

print(ans)
