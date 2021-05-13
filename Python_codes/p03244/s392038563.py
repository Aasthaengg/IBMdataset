import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import Counter

#参考 https://atcoder.jp/contests/abc111/submissions/14666502

n = int(input())
v = list(map(int, input().split()))

v0 = v[0:n-1:2]
v1 = v[1:n:2]

c0 = Counter(v0).most_common()
c1 = Counter(v1).most_common()


if len(set(v0)) == len(set(v1)) == 1:
    if c0[0] == c1[0]:
        ans = len(v0)
    else:
        ans = 0
else:
    if c0[0] != c1[0]:
        ans = n - c0[0][1] - c1[0][1]
    else:
        ans = min(n - c0[0][1] - c1[1][1], n - c0[1][1] - c1[0][1])
print(ans) 