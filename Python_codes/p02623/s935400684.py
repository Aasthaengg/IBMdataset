number=list(map(int,input().split()))
N,M,K=number[0],number[1],number[2]
A=list(map(int,input().split()))
B=list(map(int,input().split()))
a=[0]
b=[0]
for i in range(1,len(A)+1):
    tmp=a[i-1]+A[i-1]
    a.append(tmp)
    
for i in range(1,len(B)+1):
    tmp=b[i-1]+B[i-1]
    b.append(tmp)

ans=0
j=M
for i in range(N+1):
    if a[i]>K:
        break
    while b[j]>K-a[i]:
        j-=1
    ans=max(ans,i+j)

print(ans)
