R,G,B,n = map(int,input().split())

ans=0
for r in range(n//R+1):
    for g in range(n//G+1):
        tmp=n-r*R-g*G
        if tmp%B==0 and tmp//B>=0:
            ans+=1

print(ans)
