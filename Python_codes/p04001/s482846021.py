from itertools import product
s=int(input())
sl=list(str(s))
n=len(sl)
ans=0
for i in product([0,1],repeat=n-1):
    
    temp=0
    for j in range(n):
        ans+=int(sl[n-j-1])*10**temp
        temp+=1
        if n-j-2>=0 and i[n-j-2]==1:
            temp=0
print(ans)