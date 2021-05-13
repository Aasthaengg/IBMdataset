from operator import itemgetter

N, M = map(int, input().split())

a = []
b = []

for i in range(M):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)

st = sorted([(a[i],b[i]) for i in range(M)], key=itemgetter(1))

ans = 0
last = -10000000

for i in range(M):
    if last <= st[i][0]:
        ans += 1
        last = st[i][1]
print(ans)