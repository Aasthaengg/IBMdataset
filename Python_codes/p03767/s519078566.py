n, *a_l = map(int, open(0).read().split())
a_l.sort(reverse = True)
ans = 0
for a in a_l[1:2*n:2]:
    ans += a
print(ans)