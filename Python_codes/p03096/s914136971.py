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
for c in C:
    a = dic[c]
    dic[c] += ans
    ans += a

print(ans % (10 ** 9 + 7))