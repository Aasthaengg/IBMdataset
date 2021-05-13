A, B, M = map(int, input().split())
PA = [int(x) for x in input().split()]
PB = [int(x) for x in input().split()]
XYC = [tuple(map(int, input().split())) for _ in range(M)]

p1 = min(PA) + min(PB)
p2 = 10 ** 10
for x, y, c in XYC:
    p2 = min(PA[x - 1] + PB[y - 1] - c, p2)

print(min(p1, p2))