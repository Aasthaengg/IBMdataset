n, C = map(int, input().split())
L = [tuple(map(int, input().split())) for _ in range(n)]
L.sort()
tmp = [[] for _ in range(C)]
for s, t, c in L:
    if tmp[c - 1]:
        if tmp[c - 1][-1][1] == s:
            tmp[c - 1][-1][1] = t
            continue
    tmp[c - 1].append([s, t])
l = []
for v in tmp:
    for i in v:
        l.append(i)
l.sort()

r = [0] * C
for s, t in l:
    for i in range(C):
        if r[i] < s:
            r[i] = t
            break
print(sum(1 for i in r if i))            