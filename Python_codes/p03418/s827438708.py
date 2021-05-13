n,k=map(int,input().split())
ans=0
if k==0:
    ans=n*n
else:
    #count a<b cases 
    for b in range(k+1,n+1):
        ans+=b-1-k+1
    #count a>b cases 
    for b in range(k+1,n+1):
        #from b+k to b+b-1 mod>=k after that cycle repeats
        steps=(n-b+1)//b
        ans+=steps*(b-k)
        rem=(n-b+1)%b
        if rem>k:
            ans+=rem-k
print(ans)

