l = list(list(input()) for _ in range(3))

ans = ''
for i in range(3):
    ans += l[i][i]

print(ans)