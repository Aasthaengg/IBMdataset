n = int(input())
a = list(map(int, input().split()))
a.sort()
l = [x//400 if x//400 <= 7 else 8 for x in a]
p = [0]*8
for i in l:
    if i < 8:
        p[i] = 1
pmin = sum(p) if sum(p) != 0 else 1
pmax = sum(p) + l.count(8)
print(pmin, pmax)