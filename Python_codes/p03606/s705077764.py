N = int(input())
lr = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for li, ri in lr:
    ans += (ri - li + 1)

print(ans)