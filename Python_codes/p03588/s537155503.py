n = int(input())
a = sorted([list(map(int, input().split())) for _ in range(n)])
cnt = a[0][0] - 1 + n + a[-1][1]

for i in range(n - 1):
    cnt += min(a[i + 1][0] - a[i][0], a[i][1] - a[i + 1][1]) - 1
print(cnt)