def mypow(x,y):
    if y==0:return 0
    return x**y
N,K = map(int,input().split())
ans = mypow(N//K,3)
if K%2==0:
    ans+=mypow((N-K//2)//K+1,3)
print(ans)