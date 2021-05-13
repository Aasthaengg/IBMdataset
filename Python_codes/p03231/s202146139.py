from fractions import gcd

N, M = list(map(int, input().split()))
S = input()
T = input()

L = (N * M) // gcd(N, M)

L1 = [0]
L2 = [0]

from collections import Counter
c = Counter()

for i in range(1, N):
    t = i * (L // N) + 1
    L1.append(t-1)

for i in range(1, M):
    t = i * (L // M) + 1
    L2.append(t-1)


d = {}
for i, li in enumerate(L1):
    d[li] = S[i]

# print(d)

ans = True

for i, li in enumerate(L2):
    if not d.get(li):
        continue
    if d[li] != T[i]:
        ans = False

# print(L1)
# print(L2)
# print(common)
# print(dic)

if ans:
    print(L)
else:
    print(-1)


