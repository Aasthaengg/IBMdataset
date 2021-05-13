n,m = map(int,input().split())
l = 0
r = n
for i in range(m):
    li,ri = map(int, input().split())
    l = max(l,li)
    r = min(r,ri)
if r < l:
    ans = 0
else:
    ans = r - l + 1
print(ans)