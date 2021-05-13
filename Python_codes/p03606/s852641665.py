n = int(input())
lr = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for i in range(n):
    l, r = lr[i]
    ans += r - l + 1

print(ans)