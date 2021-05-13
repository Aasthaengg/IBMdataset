S=input()
N=len(S)
ans=0
T=""
U=""
if N%2==0:
  T=S[:N//2]
  U=S[N//2:][::-1]
else:
  T=S[:N//2]
  U=S[N//2+1:][::-1]
for i in range(N//2):
  if T[i]!=U[i]:
    ans+=1
print(ans)