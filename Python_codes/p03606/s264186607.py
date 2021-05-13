N = int(input())
ans = 0
for _ in range(N):
    li, ri = map(int, input().split())
    ans += (ri - li + 1)

print(ans)
