N = int(input())
A = [int(input()) for _ in range(N)]
A=sorted(A)
 
ans=0
cnt=1
tmp=A[0]
 
for i in range(1,N):
    if A[i]==tmp:
        cnt+=1
    else:
        if cnt%2!=0:
            ans+=1
        cnt=1
    tmp=A[i]
    
if cnt%2==1:
    ans+=1
print(ans)