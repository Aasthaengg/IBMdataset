from collections import Counter
from itertools import combinations as comb

N = int(input())
d = Counter()
for _ in range(N):
    s = input()
    d[s[0]] += 1

ans = 0
for i, j, k in comb(["M","A","R","C","H"], 3):
    ans += d[i]*d[j]*d[k]
print(ans)
