n,k=map(int,input().split())
cnt=0
for b in range(k+1,n+1):
    if n%b>=k:
        if k==0:
            cnt+=(b-k)*(n//b)+(n%b-k)
        else:
            cnt+=(b-k)*(n//b)+(n%b-k+1)
    else:
        cnt+=(b-k)*(n//b)

print(cnt)