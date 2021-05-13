n = int(input())
p = list(map(int, input().split()))

ans = 0
for i in range(1, n - 1):
    is_asc = p[i - 1] < p[i] < p[i + 1]
    is_desc = p[i - 1] > p[i] > p[i + 1]
    if is_asc or is_desc:
        ans += 1

print(ans)
