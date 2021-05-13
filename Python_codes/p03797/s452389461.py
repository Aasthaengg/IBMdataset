n,m = map(int,input().split())
ans = 0
re = m - 2*n
if m < 2:
    ans = 0
elif m >= 2 and re > 0:
    ans += n + re//4
else:
    ans += m//2
print(ans)