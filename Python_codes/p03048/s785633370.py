R,G,B,N=map(int,input().split())

ans=0
for r in range(N//R+1):
  for g in range(N//G+1):
    if 0<=N-r*R-g*G and (N-r*R-g*G)%B==0:
      #print(r,g,(N-r*R+g*G)//B)
      ans += 1
      
print(ans)