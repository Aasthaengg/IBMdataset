n, t = map(int, input().split())
T = list(map(int, input().split()))
ans = 0
x_ = 0
for x in T:
    if x-x_ >= t:
        ans += t
    else:
        ans += x-x_
    x_ = x
ans += t
print(ans)
