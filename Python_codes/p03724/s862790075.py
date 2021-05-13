n, m = map(int, input().split())
cnt = [0 for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    cnt[a] = (cnt[a] + 1) % 2
    cnt[b] = (cnt[b] + 1) % 2
if 1 in cnt:
    print("NO")
else:
    print("YES")
