N, T, *t_l = map(int, open(0).read().split())
ans = 0
t_before = 0
for t in t_l:
    ans += min(t-t_before, T)
    t_before = t
print(ans+T)