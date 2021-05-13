s=input()
l=len(s)
ans=int(s[l-1])*(2**(l-1))
ak=1
sk=0

for i in range(2**(l-1)):
    for j in range(l-2,-1,-1):
        if (i>>j)&1==1:
            ak=1
        else:
            ak*=10
        sk=int(s[j])*ak
        ans+=sk
    ak=1

print(ans)