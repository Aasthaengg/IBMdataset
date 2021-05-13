R,G,B,N=map(int,input().split())
ans=0
for r in range(3000+1):
  for g in range(3000+1):
    temp=r*R+g*G
    if N>=temp and (N-temp)%B==0:
      ans+=1
print(ans)
