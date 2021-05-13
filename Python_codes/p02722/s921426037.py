N=int(input())
P=0
def f(x):
  r=[]
  for i in range(1,int(x**0.5)+1):
    if x%i==0:
      r.append(i)
      if x!=i*i:
        r.append(x//i)
  return r

A=f(N)
M=0
for i in range(len(A)):
  if A[i]==1:
    continue
  M=N
  while M%A[i]==0:
    M//=A[i]
  if M%A[i]==1:
    P+=1
P+=len(f(N-1))-1
print(P)