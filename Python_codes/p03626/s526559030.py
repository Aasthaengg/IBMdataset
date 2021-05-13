mo=10**9+7
n=int(input())+1
s=input()+' '

S=[]
p=s[0]
i=0
while i<n-1:
    c=s[i+1]
    if c==p:
        S+=[2]
        i+=2
    else:
        S+=[1]
        i+=1
    if i<n:
        p=s[i]

p=S.pop()
if p==1:
    ans=3
else:
    ans=6
while S:
    c=S.pop()
    if (p,c)==(1,1):
        ans*=2
    elif (p,c)==(1,2):
        ans*=2
    elif (p,c)==(2,2):
        ans*=3
    elif (p,c)==(2,1):
        ans*=1
    ans%=mo
    p=c
print(ans)
