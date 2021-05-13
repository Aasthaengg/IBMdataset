from collections import Counter

N = int(input())
S = [input() for _ in range(N)]
l = Counter(S)
MAXNUM = max(l.values())

for s in sorted(list(set(S))):
    if l[s] == MAXNUM:
        print(s)