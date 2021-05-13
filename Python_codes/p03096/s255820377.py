import sys
from collections import defaultdict

N = int(input())
C = [0]
for _ in range(N):
    c = int(sys.stdin.readline())
    if C[-1] == c:
        continue
    else:
        C.append(c)

ans = 1
dic = defaultdict(lambda: 0)
mod = 10 ** 9 + 7
for c in C:
    a = dic[c]
    dic[c] += ans
    ans = (ans + a) % mod

print(ans % mod)
