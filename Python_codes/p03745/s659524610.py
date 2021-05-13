N=int(input())
A=list(map(int,input().split()))
zougen = 4 #0は変化無し、1は減少、２は増加、4は未決定
ans=1
for i in range(N-1):
    if zougen==4:
        if A[i]-A[i+1]<0:
            zougen = 2
        elif A[i]-A[i+1]>0:
            zougen = 1
        else:
            zougen =0
    if A[i]-A[i+1]<0:
        if zougen == 1:
            ans+=1
            zougen=4
        if zougen == 0:
            zougen =2
    if A[i]-A[i+1]>0:
        if zougen == 2:
            ans+=1
            zougen=4
        if zougen ==0:
            zougen = 1
print(ans)