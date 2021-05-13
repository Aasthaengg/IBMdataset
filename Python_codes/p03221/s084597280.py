N, M = map(int, input().split())
PY = [list(map(int, input().split())) for _ in range(M)]

A = [[] for _ in range(N+1)]

for i, py in enumerate(PY):
    A[py[0]].append([py[1], i])

City = []
for i in range(N+1):
    A[i] = sorted(A[i])
    for j, a in enumerate(A[i]):
        pref = i
        city = j+1
        City.append([a[1], str(pref).zfill(6) + str(city).zfill(6)])

City = sorted(City)
for city in City:
    print(city[1])