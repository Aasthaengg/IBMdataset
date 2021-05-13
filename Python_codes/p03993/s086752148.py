from collections import Counter
n = int(input())
A = list(map(int, input().split()))
p = []
for i, a in enumerate(A):
    idx = i+1
    if a>idx:
        a,idx = idx, a
    p.append((a, idx))
c = Counter(p)
ans = 0
for k,v in c.items():
    if v==2:
        ans += 1
print(ans)