from collections import defaultdict

N = int(input())
S = input()
Q = int(1e9 + 7)

d = defaultdict(int)

for s in S:
    d[s] += 1

ans = 1
for k, v in d.items():
    ans *= (v + 1)
    ans %= Q
ans -= 1
print(ans)