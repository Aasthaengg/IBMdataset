N,K=map(int,input().split())
a=0
for i in range(K+1,N+1):
    t=N//i
    n=N-t*i
    a+=t*(i-K)
    if K:
        a+=max(0,n-K+1)
    else:
        a+=n
print(a)