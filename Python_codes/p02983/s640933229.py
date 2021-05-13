l, r = map(int, input().split())
mod = 2019
ans = 1001001001
for i in range(l, min(r+1, l+2020)):
    for j in range(i+1, min(r+1, i+1+2020)):
        ans = min(ans , i*j%mod)
print(ans)