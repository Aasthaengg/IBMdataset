from collections import defaultdict
N = int(input())

c = defaultdict(int)

for _ in range(N):
    c[int(input())] ^= 1

res = 0
for v in c.values():
    if v:
        res += 1

print(res)