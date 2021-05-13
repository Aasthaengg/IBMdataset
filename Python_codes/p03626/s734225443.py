n=int(input())
s1=input()
s2=input()
if n>1:
    if s1[0]==s1[1]:
        i=0
    else:
        i=1
else:
    i=1
ans=3

flag=False
while i<n:
    if i<n-1:
        if s1[i]==s1[i+1]:
            if flag:
                ans*=3
                i+=2
            else:
                ans*=2
                i+=2
                flag=True
        else:
            if flag:
                flag=False
                i+=1
            else:
                ans*=2
                i+=1
    else:
        if flag:
            flag=False
            i+=1
        else:
            ans*=2
            i+=1
print(ans%(10**9+7))