def yakusu(x):
    A=[]
    for i in range(1,x+1):
        if x%i==0:
            A.append(i)
    return(len(A))
    
n=int(input())
ans=0

for j in range(1,n+1,2):
    if yakusu(j)==8:
        ans+=1
print(ans)