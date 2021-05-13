N = int(input())
lr = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for i, j in lr:
    ans += j - i + 1

print(ans)