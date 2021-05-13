N=int(input())
A=list(map(int,input().split()))

pre=A[0]
ans=0

for i in range(1,len(A)):
    if pre==A[i]:
        ans+=1
        pre=101
    
    else:
        pre=A[i]
print(ans)