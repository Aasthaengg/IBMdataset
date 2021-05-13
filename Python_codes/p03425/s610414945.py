import itertools
N = int(input())
S = [input() for _ in range(N)]
d = {'M':[], 'A':[], 'R':[], 'C':[], 'H':[]}

for s in S:
    for c in ['M', 'A', 'R', 'C', 'H']:
        if s.startswith(c):
            d[c] += [s]

num = {k: len(d[k]) for k in ['M', 'A', 'R', 'C', 'H']}

ans = 0
for v in itertools.combinations(['M', 'A', 'R', 'C', 'H'], 3):
    tmp = 1
    for c in v:
        tmp *= num[c]
    ans += tmp
print(ans)