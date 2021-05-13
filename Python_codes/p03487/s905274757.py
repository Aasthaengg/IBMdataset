from collections import Counter
n = int(input())
ls = list(map(int,input().split()))
c = Counter(ls)
p = 0
for s,t in c.items():
    if s > t:
        p += t
    elif s < t:
        p += t - s
print(p)