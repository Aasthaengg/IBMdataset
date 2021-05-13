L,R=list(map(int, input().split()))
M=2019
if R-L==1:
  print(((R%M)*(L%M))%M)
  exit()
if L//M!=R//M:
  print(0)
  exit()
L=L%M
R=R%M
ans=M
for i in range(L,R+1):
  for j in range(i+1,R+1):
    ans=min(ans,(i*j)%M)
print(ans)
