N = int(input())

S = [''.join(sorted(input())) for _ in range(N)]

table = {}

ans = 0
for s in S:
    if s in table:
        table[s] += 1
    else:
        table[s] = 1

for k in table:
    ans += table[k] * (table[k] - 1)

ans //= 2
print(ans)