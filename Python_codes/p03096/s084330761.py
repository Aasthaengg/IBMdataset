from collections import defaultdict
N = int(input())
tmp = [int(input()) for _ in range(N)]
mod = 10 ** 9 + 7
C = []
for c in tmp:
    if not C:
        C.append(c)
        continue
    if C[-1] != c:
        C.append(c)
N = len(C)

last = defaultdict(int)
ans = 1

for c in C:
    ans += last[c]
    ans %= mod
    last[c] = ans

print(ans)
