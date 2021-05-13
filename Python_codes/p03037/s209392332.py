n, m = map(int, input().split())
l, r = 1, 10**5

for i in range(m):
    ll, rr = map(int, input().split())
    l = max(l, ll)
    r = min(r, rr)

if l > r:
    print(0)
else:
    print(r-l+1)
