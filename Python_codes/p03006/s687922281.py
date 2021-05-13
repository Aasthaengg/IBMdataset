n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
t = []
for i in range(n):
    for j in range(n):
        if not i == j:
            t.append([s[i][0] - s[j][0], s[i][1] - s[j][1]])
ans = n
for i in range(pow(n, 2) - n):
    cnt = 0
    for j in range(pow(n, 2) - n):
        if t[i][0] == t[j][0] and t[i][1] == t[j][1]:
            cnt += 1
    ans = min(ans, n - cnt)
print(ans)