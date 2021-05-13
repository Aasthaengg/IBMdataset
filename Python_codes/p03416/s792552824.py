ans=0
A,B=map(int,input().split())
for i in range(A,B+1):
  k=str(i)
  if k[0]==k[4] and k[1]==k[3]:
    ans+=1
print(ans)