n,m = map(int, input().split())

ab = [list(map(int, input().split())) for _ in range(m)]
ab = sorted(ab, key=lambda x:x[1])

min_island = -float('inf')
ans = 0
for i in ab:
    if min_island <= i[0]:
        ans += 1
        min_island = i[1]
print(ans)