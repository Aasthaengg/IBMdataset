n=int(input())

l=list(map(float,input().split()))
k=[0]*(n+1)
k[0]=1
for p in l:
    for j in range(n,-1,-1):
        k[j]*=(1-p)
        if j!=0:k[j]+=k[j-1]*p

print(sum(k[n//2+1:]))