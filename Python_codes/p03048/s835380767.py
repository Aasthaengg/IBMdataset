R,G,B,n=map(int, input().split())
ans=0

for r in range(n+1):
    if r%R==0:
        for g in range(n+1-r):
            b = n-r-g
            if b%B==0 and r%R==0 and g%G==0:
                ans+=1

print(ans)
