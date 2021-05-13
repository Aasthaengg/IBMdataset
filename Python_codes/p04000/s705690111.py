H, W, N = map(int, input().split())
S = set()
toCheck = set()
rs = [0] * 10
for _ in range(N):
    a, b = map(int, input().split())
    S.add((a, b))
    for i in range(3):
        for j in range(3):
            toCheck.add((a - i, b - j))

for a, b in toCheck:
    if a + 2 > H or b + 2 > W or b < 1 or a < 1:
        continue
    cnt = 0
    for i in range(3):
        for j in range(3):
            na, nb = a + i, b + j
            if (na, nb) in S:
                cnt += 1
    rs[cnt] += 1

total = max(0, H - 2) * max(0, W - 2)
rs[0] = total - sum(rs[1:])
for it in rs:
    print(it)


