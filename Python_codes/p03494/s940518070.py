n=int(input())
A=list(map(int, input().split()))
ans=float("inf")
for i in range(n):
    cnt = 0
    while A[i]%2==0:
        A[i]=A[i]//2
        cnt+=1
    ans=min(ans,cnt)
print(ans)