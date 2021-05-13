from collections import Counter

n=int(input())
a=list(map(int,input().split()))

c=Counter(a)
ans=1
if n%2==1:
    for i in range(n):
        if i%2==1 and c[i]>0:
            ans=0
            break
        elif i%2==0 and c[i]==2:
            ans*=2
            ans%=1000000007
        if i==0 and c[i]!=1:
            ans=0
            break
else:
    for i in range(n):
        if i%2==0 and c[i]>0:
            ans=0
            break
        elif i%2==1 and c[i]==2:
            ans*=2
            ans%=1000000007
print(ans)