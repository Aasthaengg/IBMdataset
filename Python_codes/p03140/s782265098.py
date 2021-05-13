n = int(input())
s = [input() for _ in range(3)]
ans = 0
for i in range(n):
    ans += len({s[0][i], s[1][i], s[2][i]})-1
print(ans)