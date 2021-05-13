N = int(input())
tot = 0
for d in range(1, N+1):
    nd = N//d
    tot += (d * (nd + 1) * nd) // 2

print(tot)


