H,W,K=map(int, input().split())
C=list(input()for _ in range(H))
ans=0
import itertools
tf=("Yes", "No")
l=list(itertools.product(tf, repeat=(H+W)))
black=0
for i in range(2**(H+W)):
  for j in range(H):
    for k in range(W):
      if l[i][j]=="No"and l[i][H+k]=="No"and C[j][k]=="#":
        black+=1
  if black==K:
    ans+=1
  black=0
print(ans)
