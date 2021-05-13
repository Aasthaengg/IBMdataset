from collections import Counter
N = int(input())
S = [input() for _ in range(N)]
S.sort()
n = Counter()
for s in S:
    n[s] += 1
max = max(n.values())
S = set(S)
for s in S:
    if n[s] == max:
        print(s)
