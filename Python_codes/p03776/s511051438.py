from itertools import accumulate as ac
t = 3099044504245996706400 # LCM(1..50)
N, A, B = map(int, input().split())
V = sorted([int(a) * t for a in input().split()])[::-1]
l, r = 0, 1<<200
while r - l > 1:
    m = (l+r) // 2
    if list(ac([v-m for v in V]))[A-1] >= 0:
        l = m
    else:
        r = m

fa = [1]
for i in range(1, 60):
    fa.append(fa[-1] * i)
C = lambda a, b: fa[a] // (fa[a-b] * fa[b])

print(l/t)
print(sum([C(V.count(V[i-1]), V[:i].count(V[i-1])) for i in range(A, B+1) if sum(V[:i]) == l * i]))