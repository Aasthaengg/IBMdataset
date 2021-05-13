N=int(input())
A=list(map(int, input().split()))
mod=10**9+7
if A[0]!=0:
    print(0)
    exit()
L=[1,0,0]
ans=3
for i in range(1,N):
    a=A[i]
    count=0
    add=True
    for j,l in enumerate(L):
        if a==l:
            count+=1
            if add:
                L[j]+=1
                add=False

    ans*=count
    ans%=mod
print(ans)
#print(L)
