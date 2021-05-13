D, G = map(int, input().split())
G = int(G / 100)
pc = [list(map(int, input().split())) for _ in range(D)]

N = 10 ** 9
for bit in range(2 ** D):
    S = 0
    c = 0
    A = True
    a = -1
    for i in range(D - 1, -1, -1):
        if bit & (1 << i):
            S += (i + 1) * pc[i][0] + int(pc[i][1] / 100)
            c += pc[i][0]
        elif A:
            a = i
            A = False
    if a != -1:
        for i in range(1, pc[a][0]):
            if S >= G:
                break
            S += a + 1
            c += 1
    if S >= G:
        N = min(N, c)

print(N)