N = int(input())
a = [list(map(int, input().split())) for _ in range(2)]

ans = sum(a[0]) + a[1][-1]

for i in range(1, N):
    ans = max(ans, sum(a[0][:i] + a[1][i-1:]))
print(ans)