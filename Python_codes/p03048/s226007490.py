R,G,B,N=map(int,input().split())
R,G,B=sorted([R,G,B])
ans=0
for b in range(1+N//B):
      for g in range(1+(N-b*B)//G):
            if  (N-b*B-g*G)%R==0:
                  ans+=1
print(ans)

