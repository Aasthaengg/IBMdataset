N, M = map(int, input().split())
cakes = []
for _ in range(N):
    x, y, z = map(int, input().split())
    cakes.append((x, y, z))

ans = 0
for i in range(2**3):
    op1, op2, op3 = 1, 1, 1
    for idx, j in enumerate(bin(i)[2:][::-1], 1):
        j = int(j)
        if idx == 1:
            op1 = 1 if j == 0 else -1
        elif idx == 2:
            op2 = 1 if j == 0 else -1
        elif idx == 3:
            op3 = 1 if j == 0 else -1
            
    cakes.sort(reverse=True, key=lambda x: op1 * x[0] + op2 * x[1] + op3 * x[2])
    sx, sy, sz = 0, 0, 0
    for cake in cakes[:M]:
        sx += cake[0]
        sy += cake[1]
        sz += cake[2]
    ans = max(ans, abs(sx) + abs(sy) + abs(sz))
print(ans)
