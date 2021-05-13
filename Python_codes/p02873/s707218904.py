S=input()
l=len(S)
A=[0]*(l+1)
B=[0]*(l+1)
for i in range(l):
  if S[i]=='<':
    A[i+1]=A[i]+1
  if S[l-i-1]=='>':
    B[l-i-1]=B[l-i]+1
print(sum([max(a,b) for a,b in zip(A,B)]))