n, a, b = map(int, input().split())
l = list(map(int, input().split()))
l.sort(reverse=True)
# print(l)
# print(l[:a])
print(sum(l[:a]) / a)
l_w = l[:a]
ans = 0
nCr = {}


def cmb(n, r):
    if r == 0 or r == n: return 1
    if r == 1: return n
    if (n, r) in nCr: return nCr[(n, r)]
    nCr[(n, r)] = cmb(n - 1, r) + cmb(n - 1, r - 1)
    return nCr[(n, r)]


if l[0] == l[-1]:
    for i in range(a, b + 1):
        ans += cmb(b, i)
elif l_w[0] == l_w[-1]:
    for i in range(a, min(b + 1,l.count(l_w[-1])+1)):
        ans += cmb(l.count(l_w[-1]), i)
else:
    ans = cmb(l.count(l_w[-1]), l_w.count(l_w[-1]))
print(ans)
