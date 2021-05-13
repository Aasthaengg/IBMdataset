n=int(input())
s1=input()
s2=input()
mod=10**9+7

if s1[0]==s2[0]:
    ans=3
    i=1
    flag=0
else:
    ans=6
    i=2
    flag=1

while i<n:
    if flag==0:
        if s1[i]==s2[i]:
            ans*=2
            i+=1
        else:
            ans*=2
            i+=2
            flag=1
    else:
        if s1[i]==s2[i]:
            i+=1
            flag=0
        else:
            ans*=3
            i+=2
    ans%=mod
print(ans)