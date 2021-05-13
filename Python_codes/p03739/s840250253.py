N = int(input())
A = [int(_n) for _n in input().split()]
res0 = 0
s = 0
for i, a in enumerate(A):
    s += a
    if i % 2 == 0 and s >= 0:
        res0 += s + 1
        s = -1
    elif i % 2 == 1 and s <= 0:
        res0 += -s + 1
        s = 1
res1 = 0
s = 0
for i, a in enumerate(A):
    s += a
    if i % 2 == 1 and s >= 0:
        res1 += s + 1
        s = -1
    elif i % 2 == 0 and s <= 0:
        res1 += -s + 1
        s = 1
print(min(res0,res1))