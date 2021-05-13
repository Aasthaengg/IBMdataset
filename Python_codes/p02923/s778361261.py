n = int(input())
h = list(map(int, input().split()))

a = h[0]
cnt = 0
ans = 0
for i in range(1, n):
    if h[i] <= a:
        cnt += 1
        a = h[i]
    else:
        ans = max(ans, cnt)
        a = h[i]
        cnt = 0
ans = max(ans, cnt)
print(ans)