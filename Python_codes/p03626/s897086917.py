n=int(input())
a=list(input())
b=list(input())
ans=1
i=0
f=0
mod=1000000007
while i!=n:
    if i==0:
        if a[i]==b[i]:
            i+=1
            ans*=3
            ans%=mod
            f=1
        else:
            i+=2
            ans*=6
            ans%=mod
            f=2
    else:
        if a[i]==b[i] and f==1:
            i+=1
            ans*=2
            ans%=mod
            f=1
        elif a[i]==b[i] and f==2:
            i+=1
            f=1
        elif a[i]!=b[i] and f==1:
            i+=2
            ans*=2
            ans%=mod
            f=2
        else:
            i+=2
            ans*=3
            ans%=mod
            f=2
print(ans%mod)
            
        
