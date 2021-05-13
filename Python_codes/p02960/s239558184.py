S=input()
mod=10**9+7
lst=[[0 for e in range(13)] for f in range(len(S)+1)]
lst[0][0]=1
for i in range(len(S)):
 if S[i]=="?":
  for j in range(13):
   for k in range(10):
    lst[i+1][(j*10+k)%13]+=lst[i][j]
    lst[i+1][(j*10+k)%13]%=mod
 else:
  for j in range(13):
   lst[i+1][(j*10+int(S[i]))%13]+=lst[i][j]
   lst[i+1][(j*10+int(S[i]))%13]%=mod
print(lst[len(S)][5])
