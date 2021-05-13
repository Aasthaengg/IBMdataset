from collections import Counter
N = int(input())
S = []
for _ in range(N):
    s = tuple(sorted(input()))
    S.append(s)
SS = Counter(S)
ans = 0
for v in SS.values():
    if v>=2:
        ans += v*(v-1)//2
print(ans)