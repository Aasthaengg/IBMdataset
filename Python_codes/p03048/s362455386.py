R,G,B,N=map(int,input().split())
ans=0
for i in range(N//R+1):
    zan=N-R*i
    if zan==0:
        ans+=1
        continue
    for j in range(N//G+1):
        zan2=zan-G*j
        if zan2<0:
            break
        if zan2%B==0:
            ans+=1
print(ans)