# 2020/09/26
# ACL Beginner Contest - C

# Union Find
# Define List
pl = list()

def root(in_root):
    if pl[in_root] == in_root:
        return in_root
    else:
        pl[in_root] = root(pl[in_root])
        return pl[in_root]

def isSame(in_a, in_b):
    if root(pl[in_a]) == root(pl[in_b]):
        return True
    else:
        return False

def unite(in_a, in_b):
    wk_a = root(in_a)
    wk_b = root(in_b)
    if wk_a == wk_b:
        return False
    else:
        if wk_a < wk_b:
            pl[wk_b] = wk_a
        else:
            pl[wk_a] = wk_b

# Input n, m
n, m = map(int,input().split())

# Init List
for i in range(n+1):
    pl.append(i)

# Input a, b
for i in range(m):
    a, b = map(int,input().split())
    wa = min(a, b)
    wb = max(a, b)
    unite(wa, wb)

# Count
ans = 0
for i in range(1, n+1):
    if pl[i] == i:
        ans = ans + 1

# Output
print(ans-1)
