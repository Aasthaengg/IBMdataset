n=int(input())
A=[1]
for i in range(15):
  A.append(A[-1]+4**(i+1))
B=[-2,-1]
for i in range(15):
  B.append(A[i]+1)
  B.append(A[i+1])
  B.append(-2*A[i+1])
  B.append(-2*A[i]-1)
C=[1]
for i in range(32):
  C.append(C[-1]*-2)
if n==0:
  print(0)
  exit()
if n==1:
  print(1)
  exit()
a=0
i=0
while a==0:
  if B[2*i]<=n and n<=B[2*i+1]:
    a=1
  else:
    i=i+1
ans=""
while i>=0:
  if B[2*i]<=n and n<=B[2*i+1]:
    ans=ans+"1"
    n=n-C[i+1]
    i=i-1
  else:
    ans=ans+"0"
    i=i-1
if n==0:
  ans=ans+"0"
else:
  ans=ans+"1"
print(ans)