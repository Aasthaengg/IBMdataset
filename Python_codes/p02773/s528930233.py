from collections import Counter

N = int(input())
S = [input() for _ in range(N)]

counter = Counter(S)
maxv = max(counter.values())
ans = []
for k, v in counter.items():
    if v == maxv:
        ans.append(k)

ans.sort()

for s in ans:
    print(s)
