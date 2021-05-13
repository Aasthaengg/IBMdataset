n = int(input())
S = [str(input()) for _ in range(n)]
m = int(input())
T = [str(input()) for _ in range(m)]

from collections import Counter
CS = Counter(S)
CT = Counter(T)

ans = 0
for k in CS.keys():
    if k not in CT:
        ans = max(CS[k], ans)
    else:
        ans = max(ans, max(0, CS[k]-CT[k]))
print(ans)
