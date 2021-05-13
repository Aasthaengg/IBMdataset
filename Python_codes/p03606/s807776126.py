n = int(input())
lr = [list(map(int, input().split())) for i in range(n)]

ans = 0
for l,r in lr:
  ans += r - l + 1

print(ans)