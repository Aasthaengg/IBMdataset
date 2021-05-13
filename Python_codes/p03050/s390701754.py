N=int(input())
C=int(N**0.5)
if int(N**0.5)**2==N:
    C-=1
ans=0
for i in range(1,C+1):
    if (N-i)%i==0:
        num=(N-i)//i
        if num>i:
            ans+=num
    
print(ans)