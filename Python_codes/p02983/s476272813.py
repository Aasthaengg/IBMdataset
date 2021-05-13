l, r = map(int, input().split())
mod = 2019
if r-l >= 2019:
    print(0)
else:
    ans = 2020
    for i in range(l, r+1):
        for j in range(i+1, r+1):
            if i%mod == 0 or j%mod == 0:
                ans = 0
                break
            ans = min(ans, (i*j)%mod)
        if ans == 0:
            break
    print(ans)
