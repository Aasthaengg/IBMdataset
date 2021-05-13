N, *H = map(int, open(0).read().split())

ans = 0

def split_list(l, s):
    ans = []
    while l.count(s):
        pos = l.index(s)
        ans.append(l[:pos])
        l = l[pos+1:]
    ans.append(l)
    return ans

def f(L):
    if len(L) == 0:
        return
    while L.count(0) == 0:
        global ans
        ans += 1
        L = [l - 1 for l in L]
    for m in split_list(L, 0):
        f(m)

f(H)
print(ans)