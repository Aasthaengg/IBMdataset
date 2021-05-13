def find(n):
    if root[n] == n:
        return n
    else:
        parent = root[n]
        root[n] = find(parent)
        return root[n]

def unite(x,y):
    rx = find(x)
    ry = find(y)
    if rx == ry:
        return
    else:
        root[rx] = ry

def same(x,y):
    if find(x) == find(y):
        return True
    else:
        return False

def member(x):
    root = find(x)
    return [i for i in range(n) if find(i) == root]

def member_count(x):
    return len(member(x))

n , m = map(int,input().split())
route = [tuple(map(lambda x:int(x)-1,input().split())) for i in range(m)]
ans = 0
for i in range(m):
    root = [k for k in range(n)]
    for j in range(m):
        if i == j:
            continue
        a,b = route[j]
        unite(a,b)
    if member_count(0) != n:
        ans += 1
        
print(ans)