N,K = map(int,input().split())
ans = (N//K)**3
if K%2==0:
    m = K//2
    ans += ((N+m)//K)**3
print(ans)