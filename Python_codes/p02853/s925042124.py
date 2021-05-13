X, Y = [int(n) for n in input().split()]
V = {0: 400000, 1: 300000, 2: 200000, 3: 100000}
ans = 0
for i in [X, Y]:
    ans += V.setdefault(i, 0)
print(ans+V[0] if X==1==Y else ans)
