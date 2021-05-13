n, h = map(int, input().split())
sords = [list(map(int, input().split())) for _ in range(n)]
best = sorted(sords)[-1][0]
throw_damage = 0
cnt = 0
for i in sords:
    if i[1] > best:
        throw_damage += i[1]
        cnt += 1
if throw_damage >= h:
    sords.sort(key = lambda x:(-x[1],x[0]))
    throw_damage = 0
    cnt = 0
    for i in sords:
        throw_damage += i[1]
        cnt += 1
        if throw_damage >= h:
            print(cnt)
            exit()
print(cnt + (h - throw_damage) // best + ((h - throw_damage)%best != 0))