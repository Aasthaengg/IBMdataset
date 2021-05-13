n=int(input())
alst=list(map(int,input().split()))

csum=[0]*(n+1)
xor=[0]*(n+1)

for i in range(n):
    csum[i+1]=csum[i]+alst[i]
    xor[i+1]=xor[i]^alst[i]

ans=0

for i in range(n):
    left=0
    right=i

    while abs(right-left)>0:
        center=(right+left)//2

        s=csum[i+1]-csum[center]
        x=xor[i+1]^xor[center]

        if s==x:
            right=center
        else:
            left=center+1
    
    ans+=i-right+1

print(ans)