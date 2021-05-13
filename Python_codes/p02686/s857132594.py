n=int(input())
A=[]
B=[]
c=0
for i in range(n):
  S=input()
  a=0
  b=0
  for j in range(len(S)):
    if S[j]=="(":
      a=a+1
    else:
      a=a-1
      if a<b:
        b=a
  b=b*-1
  if b==0:
    c=c+a
  elif a>=0:
    B.append([b,-1*a])
  else:
    A.append([b+a,a])
A.sort()
B.sort()
f=0
for i in range(len(B)):
  if c-B[i][0]<0:
    f=1
  c=c-B[i][1]
d=0
for i in range(len(A)):
  if d-A[i][0]<0:
    f=1
  d=d-A[i][1]
if c!=d:
  f=1
if f==0:
  print("Yes")
else:
  print("No")