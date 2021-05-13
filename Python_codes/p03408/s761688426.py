n = int(input())
S = [str(input()) for _ in range(n)]
m = int(input())
T = [str(input()) for _ in range(m)]

from collections import Counter
cs = Counter(S)
ct = Counter(T)

ans = -10**18
for k, v in cs.items():
    if k in ct:
        temp = v - ct[k]
    else:
        temp = v
    ans = max(ans, temp)
print(max(ans, 0))
