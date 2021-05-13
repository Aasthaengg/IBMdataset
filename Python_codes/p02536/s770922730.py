n, m = map(int, input().split())
pair = [i for i in range(n + 1)]
def find(x):
    if pair[x] == x:
        return x
    else:
        pair[x] = find(pair[x]) 
        return pair[x]
def same(x,y):
    return find(x) == find(y)
def unite(x,y):
    x = find(x)
    y = find(y)
    if x == y:
        return 0
    pair[x] = y
    
for i in range(m):
    a, b = map(int, input().split())
    unite(a,b)


ans = 0
for i, k in enumerate(pair[1:], 1):
    if i == k:
        ans += 1
    
print(ans - 1)

