N = int(input())
lr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for one in lr:
    ans += one[1] - one[0] + 1
print(ans)
