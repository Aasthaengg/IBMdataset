INF=10**9+7
n=int(input())
s1=input()
s2=input()
ans=1
v=0
h=0
i=0
while i!=n:
    if v==0 and h==0:
        if s1[i]==s2[i]:
            ans=3
            v=1
            i=i+1
        else:
            ans=3*2
            h=1
            i=i+2
    elif v==1:
        if s1[i]==s2[i]:
            ans=(ans*2)%INF
            i=i+1
        else:
            ans=(ans*2)%INF
            v=0
            h=1
            i=i+2
    elif h==1:
        if s1[i]==s2[i]:
            v=1
            h=0
            i=i+1
        else:
            ans=(ans*3)%INF
            i=i+2
print(ans)
