X, Y = map(int, input().split())
ans = 10**18
for i in [True, False]:
    for j in [True, False]:
        x, y = X, Y
        tot = 0
        if i: x = -x; tot += 1
        if j: y = -y; tot += 1
        if x <= y:
            ans = min(ans, tot+(y-x))
print(ans)
