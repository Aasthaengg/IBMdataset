from collections import Counter
n = int(input())
sl = []
for i in range(n):
    s = list(input())
    s.sort()
    sl.append("".join(s))
d = Counter(sl)

def cul(n):
    return n*(n - 1)//2

ans = 0
val = d.values()
for i in val:
    if i > 1:
        ans += cul(i)
print(ans)