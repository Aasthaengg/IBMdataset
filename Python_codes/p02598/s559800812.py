n, k = map(int, input().split())
a = list(map(int, input().split()))

l, r = 0, max(a)

def ok(m):
    cut = 0
    for x in a:
        cut += (x - 1) // m
    return cut <= k

while r - l > 1:
    m = (l + r) // 2
    if ok(m):
        r = m
    else:
        l = m

print(r)