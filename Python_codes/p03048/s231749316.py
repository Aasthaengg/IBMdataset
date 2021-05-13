R,G,B,N=map(int,input().split())

ans=0
i=0
while i<=3000:
    j=0
    while j<=3000 and N-(i*R+j*G)>=0:
        if (N-(i*R+j*G))%B==0:
            ans+=1
        j+=1
    i+=1

print(ans)