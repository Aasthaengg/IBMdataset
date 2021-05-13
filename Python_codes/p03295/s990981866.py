from operator import itemgetter

N,M = map(int,input().split())

a = []
b = []

for i in range(M):
    ao,bo = map(int,input().split())
    a.append(ao)
    b.append(bo)

ab = sorted([(a[i],b[i]) for i in range(M)], key = itemgetter(1))

ans = 0
last = 0

for i in range(M):
    if last <= ab[i][0]:
        ans += 1
        last = ab[i][1]

print(ans)
