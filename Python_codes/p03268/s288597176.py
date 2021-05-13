N,K = map(int,input().split())
if K%2==0:
    k = K//2
    o = (N+k)//K
    e = N//K
    ans = e**3+o**3
else:
    ans = (N//K)**3
print(ans)    