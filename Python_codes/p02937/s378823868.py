from collections import Counter
import bisect


S = input()
S = S + S
T = input()
SC = Counter(S)
TC = Counter(T)
A = [[] for _ in range(150)]

for t in TC.keys():
    if t not in SC:
        print(-1)
        exit()

for i, s in enumerate(S):
    A[ord(s)].append(i)

N = len(S) // 2
ans = 0
now = -1

for t in T:
    At = A[ord(t)]
    x = bisect.bisect_left(At, now)
    now = At[x]
    if now + 1 >= N:
        ans += 1
    now += 1
    now %= N

print(ans * N + now)
