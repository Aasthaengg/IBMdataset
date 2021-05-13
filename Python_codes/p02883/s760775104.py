n, k = map(int, input().split())
a = list(map(int, input().split()))
f = list(map(int, input().split()))
a.sort()
f.sort(reverse=True)
costs = [(ai * fi, fi) for ai, fi in zip(a, f)]
costs.sort(reverse=True)
# l impossible, r ok
l, r = -1, costs[0][0]
while(r - l > 1):
    c = (l + r) // 2
    train = 0
    for cost, step in costs:
        if cost > c:
            train += (cost - c + step - 1) // step
    if train <= k:
        r = c
    else:
        l = c
print(r)
