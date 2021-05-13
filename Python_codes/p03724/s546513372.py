n, m = map(int, input().split())
info = [list(map(int, input().split())) for i in range(m)]

memo = {}
for i in range(m):
    if info[i][0] not in memo:
        memo[info[i][0]] = 1
    else:
        memo[info[i][0]] += 1
    if info[i][1] not in memo:
        memo[info[i][1]] = 1
    else:
        memo[info[i][1]] += 1
for i in memo:
    if memo[i] % 2 == 1:
        print("NO")
        exit()
print("YES")