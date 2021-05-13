N=int(input())
S=input()
ans=0
for i in range(1,N):
 ct=0
 ansa=0
 for j in range(N-i):
  if S[j]==S[j+i]:
   ct+=1
   ansa=max(ct,ansa)
  else:
   ct=0
 ans=max(ans,min(ansa,i))
print(ans)