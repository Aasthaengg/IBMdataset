from collections import defaultdict
import math

def comb(n, r):
    return math.factorial(n)//(math.factorial(r)*math.factorial(n-r))

n, a, b = map(int, input().split())
v = list(map(int, input().split()))

d = defaultdict(int)
for i in range(n):
    d[v[i]] += 1

keys = list(d.keys())
keys.sort(reverse=True)
cnt = 0
kind = 0
s = 0
for i in range(len(keys)):
    k = keys[i]
    kind += 1
    if cnt+d[k] < a:
        cnt += d[k]
        s += k*d[k]
    else:
        s += k*(a-cnt)
        break
print(s/a)
if kind > 1:
    print(comb(d[keys[kind-1]], a-cnt))
else:
    ans = 0
    for i in range(a, b+1):
        if d[keys[0]] < i:
            break
        ans += comb(d[keys[0]], i)
    print(ans)