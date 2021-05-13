R,G,B,N=map(int, input().split())
rmax=N//R
gmax=N//G
ans=0
for r in range(rmax+1):
  for g in range(gmax+1):
    if N-(r*R+g*G)>=0 and (N-(r*R+g*G))%B==0:
      ans+=1
print(ans)