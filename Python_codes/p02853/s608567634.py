a = list(map(int,input().split()))
ans = 0
for v in a:
    if v == 1:
        ans += 300000
    elif v == 2:
        ans += 200000
    elif v == 3:
        ans += 100000
if sum(a) == 2:
    ans += 400000
print(ans)