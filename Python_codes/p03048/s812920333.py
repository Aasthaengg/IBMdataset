R,G,B,N=map(int,input().split())
ans=0
rr=N//R+1
gg=N//G+1
bb=N//B+1
for r in range(rr):
    for g in range(gg):
        if (N-R*r-G*g)%B==0 and N-R*r-G*g>=0:
            ans+=1
        elif N-R*r-G*g<0:
            pass
print(ans)