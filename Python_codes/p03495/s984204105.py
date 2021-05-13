from collections import Counter as c
n,k=map(int,input().split())
a=list(map(int,input().split()))

b=sorted(c(a).items(),key=lambda x:x[1])
kind=len(c(a))
i=0
ans=0
while k<kind:
    ans+=b[i][1]
    kind-=1
    i+=1
print(ans)