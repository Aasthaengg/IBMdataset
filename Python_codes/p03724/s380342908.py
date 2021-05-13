n, m = map(int, input().split())
cnt = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    cnt[a] += 1
    cnt[b] += 1
for i in cnt:
    if not i % 2 == 0:
        print("NO")
        exit()
print("YES")