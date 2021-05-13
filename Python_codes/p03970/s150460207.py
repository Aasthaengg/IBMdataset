S=input()
T="CODEFESTIVAL2016"
N=len(T)

ans=0
for i in range(N):
  if S[i]!=T[i]:
    ans+=1
print(ans)