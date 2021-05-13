from collections import defaultdict

N = int(input())
SP = sorted([list(input().split()) + [i + 1] for i in range(N)])

d = defaultdict(list)

for s, p, i in SP:
    d[s].append((int(p), i))

ans = []

for k, v in d.items():
    v = sorted(v)[::-1]
    for i, j in v:
        ans.append(str(j))

print('\n'.join(ans))
