N=int(input())
S=input()
ans=0
for i in range(1000):
 l=str(i).zfill(3);k=0
 for j in range(N):
  if S[j]==l[k]:
   k+=1
   if k==3:ans+=1;break
print(ans)
