l, r = map(int, input().split())
ans = 4070306
if l <= 2019 <= r:
    ans = 0
else:
    for i in range(l, min(r, l+2019)+1):
        for j in range(i+1, min(r, i+2019)+1):
            ans = min(ans, (i*j)%2019)
print(ans)