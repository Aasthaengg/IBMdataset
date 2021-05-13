css = [input().rstrip() for _ in range(3)]

ans = ''
for i in range(3):
    ans += css[i][i]

print(ans)
