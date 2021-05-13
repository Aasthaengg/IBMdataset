n=int(input())
s=input()
t=input()
ans=1
if s[0]==t[0]:ans=3;i,b=1,1
else:ans=6;i,b=2,0
while i<n:
    if s[i]==t[i]:
        ans*=b+1
        i+=1
        b=1
    else:
        ans*=3-b
        i+=2
        b=0
print(ans%(10**9+7))