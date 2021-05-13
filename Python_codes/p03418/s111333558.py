N,K=map(int,input().split())

ans=0
for b in range(K+1,N+1):
    quo=N//b
    ans+=quo*(b-K)
    rem=N-(b*quo+K-1)#途中までの
    if rem>0:
        ans+=rem

if K==0:
    ans-=N-K#a=0(商０かつ余り0)をカウントしているので
        
print(ans)

