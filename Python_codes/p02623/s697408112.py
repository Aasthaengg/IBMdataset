n, m, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = 0
ia = -1
ib = -1

nowtime = 0
cnt = 0
for i in range(n):
    if nowtime + a[i] <= k:
        nowtime += a[i]
        cnt += 1
        ia = i
    else:
        break

ans = cnt
# print(ans, nowtime)
for i in range(m):
    while nowtime + b[i] > k and ia >= 0:
        nowtime -= a[ia]
        cnt -= 1
        ia -= 1
    if nowtime + b[i] > k:
        break
    nowtime += b[i]
    cnt += 1
    ans = max(ans, cnt)

print(ans)