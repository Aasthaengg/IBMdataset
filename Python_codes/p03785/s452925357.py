n, c, k = map(int, input().split())
t = [int(input()) for i in range(n)]
t.sort()
ans = 1
cur = t[0]
cnt = 0
for i in t:
    if i > cur + k or cnt == c:
        ans += 1
        cnt = 1
        cur = i
    else:
        cnt += 1
print(ans)