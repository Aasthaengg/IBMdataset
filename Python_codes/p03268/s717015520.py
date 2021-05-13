N, K = map(int,input().split())
tmp = tmp2 = 0
if K%2!=0:
    tmp = N//K
    print(tmp**3)
    exit()
K //= 2
tmp2 = N//K
ans = (tmp2//2)**3+(tmp2-tmp2//2)**3
print(ans)