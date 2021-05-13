n = int(input())
a = list(map(int, input().split()))

l = a[:]
while len(l) > 1:
    midx = l.index(min(l))
    r = []
    for i in range(len(l)):
        if i != midx:
            l[i] = l[i] % l[midx]
        if l[i] != 0:
            r.append(l[i])
    l = r[:]
print(l[0])