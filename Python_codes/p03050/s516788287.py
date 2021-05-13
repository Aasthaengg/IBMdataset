# N//m==N%m=k
# N=k*m+k=k(m+1)=kM
N=int(input())
arr=[]
for i in range(1,int(N**0.5)+1):
    if N%i==0:
        arr.append(N//i)
        if N//i!=i:
            arr.append(i)
arr.sort()

ans=0
for M in arr:
    m=M-1
    if m==0:continue
    if N%m==N//m:
        ans+=m
print(ans)
        
