n, *h = map(int, open(0).read().split())
left = h[0]
ans = 0
cnt = 0
for i in range(1,n):
    if left >= h[i]:
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 0
    left = h[i]
print(max(ans, cnt))