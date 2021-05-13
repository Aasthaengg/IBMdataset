n=int(input())
s=input()
p,q,r=0,1,0
for i in range(n):
    if r==0:
        if i+1<n and s[i]==s[i+1]:
            if p==0:q*=6
            elif p==1:q*=3
            else:q*=2
            r=1
            p=1
        else:
            if p==0:q*=3
            elif p==2:q*=2
            p=2
    else:
        r=0
print(q%(10**9+7))