n=int(input())
A=list(map(int,input().split()))
cnt=1
ans=0
for i in range(len(A)):
    if A[i]==cnt:
        cnt+=1
    else:
        ans+=1
if ans==len(A):
    print(-1)
else:
    print(ans)