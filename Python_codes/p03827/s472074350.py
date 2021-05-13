N=int(input())
S=input()
x=0
M=0
for i in range(len(S)):
  if S[i]=='I':
    M=max(x+1,M)
    x=x+1
  else:
    x=x-1
print(M)