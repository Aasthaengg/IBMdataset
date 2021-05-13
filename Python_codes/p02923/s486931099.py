n = int(input())
(*h,) = map(int, input().split())

a = h[0]
cnt, ans = 0, 0
for i in range(1, n):
    if a >= h[i]:
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 0
    a = h[i]
print(max(ans, cnt))