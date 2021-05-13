N=input()
M=input()
N=list(str(N))
M=list(str(M))
ans=[]
if len(N)>len(M):
  for i in range(len(N)-1):
    ans.append(N[i])
    ans.append(M[i])
  ans.append(N[-1])
else:
  for i in range(len(N)):
    ans.append(N[i])
    ans.append(M[i])
print("".join(ans))