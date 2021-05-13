n, t = (int(x) for x in input().split())
t_l = [int(x) for x in input().split()]
ans = s = 0
for t_i in t_l:
    if s <= t_i:
        ans += t
    else:
        ans += (t_i - s) + t
    s = t_i + t
print(ans)