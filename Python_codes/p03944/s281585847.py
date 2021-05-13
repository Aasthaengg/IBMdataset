w, h, n = map(int, input().split())
ll_x, ll_y, tr_x, tr_y = 0, 0, w, h
for q in range(n):
    x, y, a = map(int, input().split())
    if a == 1:
        ll_x = max(ll_x, x)
    elif a == 2:
        tr_x = min(tr_x, x)
    elif a == 3:
        ll_y = max(ll_y, y)
    elif a == 4:
        tr_y = min(tr_y, y)
ans = (tr_x - ll_x) * (tr_y - ll_y)
if (ll_x > tr_x) or (ll_y > tr_y):
    ans = 0
print(ans if ans > 0 else 0)