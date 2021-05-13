from collections import Counter

N,*a = map(int, open(0).read().split())
c = Counter(a)
ans = 0
for x in c.items():
    if x[1] >= x[0]:
        ans += x[1] - x[0]
    else:
        ans += x[1]
print(ans)