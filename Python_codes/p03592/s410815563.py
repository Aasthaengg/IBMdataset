n, m, k = map(int, input().split())

ans = "No"
for i in range(n + 1):
    for j in range(m + 1):
        cnt = (n - i) * j + (m - j) * i
        if cnt == k:
            ans = "Yes"

print(ans)
