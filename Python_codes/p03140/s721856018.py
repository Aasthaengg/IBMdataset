n = int(input())
a = list(input())
b = list(input())
c = list(input())
def how_many_changes(p,q,r):
    if p != q and q != r and r != p:
        return 2
    if p == q != r or q == r != p or r == p != q:
        return 1
    else:
        return 0
ans = 0
for i in range(n):
    ans += how_many_changes(a[i], b[i], c[i])
print(ans)