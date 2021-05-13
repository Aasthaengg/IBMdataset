N, M = map(int, input().split())

pref = []
for i in range(M):
    pp, yy = map(int, input().split())
    pref.append((yy, pp, i))

pref.sort(key=lambda tup:tup[0])

count = [0]*(N+1)
names = ['']*(M+1)
for i in range(M):
    yy, pp, id = pref[i]
    count[pp] += 1
    names[id] = '{:06d}{:06d}'.format(pp, count[pp])

for id in range(M):
    print(names[id])
