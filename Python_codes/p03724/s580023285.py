n, m = map(int, input().split())
cnt = [0] * n
for i in range(m):
    a, b = map(int, input().split())
    cnt[a - 1] += 1
    cnt[b - 1] += 1

ans = "YES"
for i in range(n):
    if cnt[i] % 2 == 1:
        ans = "NO"
        break

print(ans)