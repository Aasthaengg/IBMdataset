N=int(input())
S=[]
ans=0
for i in range(1,N):
 for j in range(i+1,N+1):
  S.append([i,j])
  ans+=1
if N%2==1:
 for i in range(1,N//2+1):
  S.remove([i,N-i])
  ans-=1
else:
 for i in range(1,N//2+1):
  S.remove([i,N+1-i])
  ans-=1
print(ans)
for j in S:
 print(*j)
