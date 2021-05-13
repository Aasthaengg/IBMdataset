n=int(input())
b=[int(i) for i in input().split()]
ind=1
ans=0
tmp=b[0]
for i in range(n):
    ans+=ind-i
    while ind<n:
        if tmp+b[ind]!=tmp^b[ind]:
            tmp-=b[i]
            break
        else:
            tmp+=b[ind]
            ind+=1
            ans+=1
print(ans)

    








