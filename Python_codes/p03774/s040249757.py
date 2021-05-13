N, M = map(int, input().split())

persons = []
checks = []
for _ in range(N):
    persons.append(list(map(int, input().split())))
for _ in range(M):
    checks.append(list(map(int, input().split())))

for px, py in persons:
    i = 0
    min_dist = -1
    for k, (cx, cy) in enumerate(checks):
        m = abs(px-cx) + abs(py-cy)
        if k==0 or (k>0 and m < min_dist):
            i = k
            min_dist = m
    print(i+1)

