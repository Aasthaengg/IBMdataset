from collections import defaultdict

N, K = map(int, input().strip().split(" "))

d = defaultdict(int)

for i in [int(i) for i in input().strip().split(" ")]:
    d[i] += 1

if len(d.keys()) <= K:
    print(0)
else:
    cnt = len(d.keys()) - K
    n = 0
    for v in sorted(d.values())[:cnt]:
        n += v
    print(n)
