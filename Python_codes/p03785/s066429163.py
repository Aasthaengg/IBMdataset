n, c, k = map(int, input().split())
t = sorted(list(int(input()) for _ in range(n)))

ans = 1
now = t[0]
cnt = 0
for i in t:
    cnt += 1
    if i > now + k or cnt > c:
        ans += 1
        cnt = 1
        now = i

print(ans)