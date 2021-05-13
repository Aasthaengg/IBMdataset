from collections import defaultdict

n = int(input())
V = list(map(int, input().split()))

if len(set(V)) == 1:
    print(n // 2)
    exit()

d0, d1 = defaultdict(int), defaultdict(int)

for i, v in enumerate(V):
    if i % 2 == 0:
        d0[v] += 1
    else:
        d1[v] += 1

d0_ = sorted(d0.items(), key=lambda x: -x[1])
d1_ = sorted(d1.items(), key=lambda x: -x[1])

a0, n0 = d0_[0]
a1, n1 = d1_[0]

if a0 != a1:
    ans = n - n0 - n1
else:
    if n0 > n1:
        m1 = d1_[1][1]
        ans = n - n0 - m1
    elif n0 < n1:
        m0 = d0_[1][1]
        ans = n - m0 - n1
    else:
        m0 = d0_[1][1]
        m1 = d1_[1][1]
        ans = n - n0 - max(m0, m1)

print(ans)