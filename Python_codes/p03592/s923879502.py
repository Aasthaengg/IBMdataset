# https://atcoder.jp/contests/code-festival-2017-quala/tasks/code_festival_2017_quala_b

n, m, k = map(int, input().split())

s = set()
for i in range(n + 1):
    for j in range(m + 1):
        t = i * (m - j) + j * (n - i)
        if t <= n * m:
            s.add(t)
if k in s:
    print('Yes')
else:
    print('No')
