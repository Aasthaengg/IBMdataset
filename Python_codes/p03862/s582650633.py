N, x = map(int, input().split())
alist = list(map(int, input().split()))
ans = 0
if alist[0] > x:
    ans += alist[0] - x
    alist[0] = x
for i in range(1, N):
    cost = alist[i] + alist[i-1]
    if cost > x:
        over = cost - x
        ans += over
        alist[i] -= over
print(ans)