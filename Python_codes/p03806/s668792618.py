N, A, B = map(int, input().split())
chem = []
for i in range(N):
    a, b, c = map(int, input().split())
    chem.append((a, b, c))

MAXX = N*10 + 1
MAXMONEY = 100*MAXX
money = [[MAXMONEY]*MAXX for _ in range(MAXX)]
ans = MAXMONEY

money[0][0] = 0
for i in range(N):
    a, b, cc = chem[i]
    for c1 in range(MAXX-1, -1, -1):
        for c2 in range(MAXX-1, -1, -1):
            if money[c1][c2] < MAXMONEY:
                newm = money[c1][c2] + cc
                if (c1 + a < MAXX) and (c2+b < MAXX) and (money[c1+a][c2+b] > newm):
                    money[c1 + a][c2 + b] = newm


rr = int(min((MAXX+0.9*A)//A, (MAXX+0.9*B)//B))
for bai in range(1, rr):
    if money[A*bai][B*bai] < ans:
        ans = money[A*bai][B*bai]

if ans >= MAXMONEY: ans = -1
print(ans)
