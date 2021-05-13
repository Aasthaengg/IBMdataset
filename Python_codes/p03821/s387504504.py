n = int(input())
ls = [tuple(map(int, input().split())) for _ in range(n)]
ans = 0
for i in reversed(range(n)):
    ans += (ls[i][1] - (ls[i][0] + ans) % ls[i][1]) % ls[i][1]
print(ans)
