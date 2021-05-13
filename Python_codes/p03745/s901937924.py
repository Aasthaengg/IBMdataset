n=int(input())
A=list(map(int,input().split()))
zo=0 ; mi=0 ;ans=1
for i in range(n-1):
    #print(zo,mi,i)
    if zo==mi==0:
        if A[i]==A[i+1]:
            continue
        elif A[i]>A[i+1]:
            mi=1; continue
        else:
            zo=1;continue
    if zo:
        if A[i+1]<A[i]:
            zo=0; ans+=1
    if mi and A[i]<A[i+1]:
        mi=0 ; ans+=1
print(ans)