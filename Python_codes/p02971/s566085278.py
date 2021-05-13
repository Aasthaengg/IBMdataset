N=int(input())
A=[]
for i in range(N):
  A.append(int(input()))
s=sorted(A,reverse=True)
for i in range(N):
  if A[i]!=s[0]:
    print(s[0])
  else:
    print(s[1])