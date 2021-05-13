# https://atcoder.jp/contests/keyence2019/tasks/keyence2019_c

import sys
n = int(input())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]

for i in range(n):
    if A[i] < B[i]:
        break
else:
    print(0)
    sys.exit()
s = 0
ans = 0
t = []
for i in range(n):
    if A[i] < B[i]:
        s += B[i] - A[i]
        ans += 1
    t.append(A[i] - B[i])
t.sort(reverse=True)

for i in range(n):
    if s < 0:
        break
    s -= t[i]
    ans += 1
if s > 0:
    print(-1)
else:
    print(ans)
