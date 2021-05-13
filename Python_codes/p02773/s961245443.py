from  collections import Counter
N = int(input())
S = [input() for _ in range(N)]

S = dict(Counter(S))
m = max(S.values())

ans = []
for s, v in S.items():
    if v == m:
        ans.append(s)
ans.sort()

for a in ans:
    print(a)
