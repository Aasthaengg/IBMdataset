n=int(input())
s1=input()
s2=input()
if s1[0]==s2[0]:
    i=1
else:
    i=0
ans=3

flag=False
while i<n:
    if s1[i]==s2[i]:
        if flag:
            flag=False
            i+=1
        else:
            ans*=2
            i+=1
    else:
        if flag:
            ans*=3
            i+=2
        else:
            ans*=2
            i+=2
            flag=True

print(ans%(10**9+7))