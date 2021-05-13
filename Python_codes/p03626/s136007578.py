n=int(input())
a=input()
b=input()

ans=0
MOD= 1000000007
cnt=0
ptn=-1
while cnt<n:
    if a[cnt]==b[cnt]:
        if cnt==0:
            ans=3
            ptn=0
        else:
            if ptn==0:
                ans*=2
                ptn=0
            else:
                ans*=1
                ptn=0
        cnt+=1
    else:
        if cnt==0:
            ans=6
            ptn=1
        else:
            if ptn==0:
                ans*=2
                ptn=1
            else:
                ans*=3
                ptn=1
        cnt+=2
    ans%=MOD

print(ans)