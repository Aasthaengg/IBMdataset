n = int(input())
a_s = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for a in a_s:
    ans += sum(a)

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        for k in range(n):
            if i == k or j == k:
                continue
            if a_s[i][j] > a_s[i][k] + a_s[j][k]:
                print(-1)
                exit()
            if a_s[i][j] == a_s[i][k] + a_s[j][k]:
                ans -= a_s[i][j]
                break

ans //= 2
print(ans)