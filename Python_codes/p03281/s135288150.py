N=int(input())
if N<105:
    print(0)
elif N==105:
    print(1)
else:
    ans=1
    for n in range(106,N+1):
        if n%2:
            K=n//2
            y=0
            #print(n,K)
            for k in range(2,K+1):
                if n%k==0:
                    y+=1
                    #print(k)
            if y==6:
                #print(n)
                ans+=1
    print(ans)