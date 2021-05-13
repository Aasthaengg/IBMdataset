n=int(input())
A=list(map(int,input().split()))
now=A[0]
cnt=0
ans=-1
for i in range(1,n):
    if A[i]<=now:
        cnt+=1
        now=A[i]
    else:
        ans=max(ans,cnt)
        cnt=0
        now=A[i]
print(max(ans,cnt))