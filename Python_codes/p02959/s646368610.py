n = int(input())
a, b = [list(map(int, input().split())) for _ in range(2)]

tmp, cnt = 0, 0
for i in range(n):
    tmp = min(a[i] - tmp, b[i])
    cnt += tmp
    tmp = min(a[i + 1], b[i] - tmp)
    cnt += tmp
print(cnt)