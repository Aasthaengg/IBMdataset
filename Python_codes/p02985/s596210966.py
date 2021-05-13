def factorial(n, mod):
    fac = [0] * (n + 1)
    inv = [0] * (n + 1)
    fac[0], inv[0] = 1, 1
    for i in range(1, n + 1):
        fac[i] = fac[i-1] * i % mod
        inv[i] = inverse(fac[i], mod)
    return fac, inv

def inverse(a, mod):
    a %= mod # 除数が正なら正になる
    p = mod
    x, y = 0, 1
    while a > 0:
        n = p // a
        p, a = a, p % a, 
        x, y = y, x - n * y
    return x % mod # 除数が正なら正になる

mod = 1000000007
n, k = map(int, input().split())
        
nodes = [[] for _ in range(n)]

branch_n = [0] * n
for i in range(n-1):
    a, b = map(lambda x : int(x) - 1, input().split())
    nodes[a].append(b)
    nodes[b].append(a)

if len(nodes[0]) >= k:
    print(0)
    quit()
stack = nodes[0][:]
visited = {0}
fac, inv = factorial(k, mod)
ans = fac[k] * inv[k-len(nodes[0])-1] % mod
while stack:
    i = stack.pop()
    visited.add(i)
    m = len(nodes[i])
    if m >= k:
        print(0)
        quit()
    ans = ans * fac[k-2] % mod * inv[k-1-m] % mod
    for j in nodes[i]:
        if not j in visited:
            stack.append(j)
print(ans)