n=int(input())
print(0)
A=[-1]*n
S=input()
if S=="Vacant":
  exit()
elif S=="Male":
  A[0]=0
else:
  A[0]=1
l=0
r=n
while r-l!=0:
  mid=(l+r)//2
  print(mid)
  S=input()
  if S=="Vacant":
    exit()
  elif S=="Male":
    A[mid]=0
  else:
    A[mid]=1
  if (mid-l)%2!=(A[l]+A[mid])%2:
    r=mid
  else:
    l=mid