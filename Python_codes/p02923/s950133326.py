n=int(input())
h=list(map(int,input().split()))
ans=0
tmp=h[0]
tt=0
for i in range(n-1):
    if h[i+1]<=tmp:
        tmp=h[i+1]
        tt+=1
        if tt>ans:
            ans=tt
    else:
        tmp=h[i+1]
        tt=0
print(ans)