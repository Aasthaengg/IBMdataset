import math

n, k = map(int, input().split())
l = []
logk = math.log2(k)
for i in range(1, n + 1):
    p = math.ceil(logk - math.log2(i))
    p = p if p >= 0 else 0
    l.append(p)
maxl = max(l)
l = list(map(lambda x: 2**(maxl-x), l))
print(sum(l)/(n*2**maxl))