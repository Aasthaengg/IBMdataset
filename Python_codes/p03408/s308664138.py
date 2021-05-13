from collections import Counter
N = int(input())
s = [input() for _ in range(N)]
M = int(input())
t = [input() for _ in range(M)]
cs = Counter(s)
ct = Counter(t)

ans = 0
for k, v in cs.items():
    tmp = v
    if k in ct.keys():
        tmp -= ct[k]

    ans = max(ans, tmp)

print(ans)
