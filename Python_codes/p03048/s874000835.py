R,G,B,N=map(int,input().split())

ans=0
for r in range(N+1):
    for g in range(N+1):
        if R*r+G*g>N:
            break
        if (N-R*r-G*g)%B==0:
            ans+=1
print(ans)