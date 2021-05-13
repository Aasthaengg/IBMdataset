n,k=map(int,input().split())
S=list(input())
A=[]
a=1
c=0
for i in range(n):
  if int(S[i])==a:
    c=c+1
  else:
    A.append(c)
    a=(a+1)%2
    c=1
A.append(c)
if S[-1]=="0":
  A.append(0)
aa=len(A)
if k>=((aa-1)//2):
  print(n)
else:
  ans=0
  a=0
  for i in range(2*k+1):
    a=a+A[i]
  if a>ans:
    ans=a
  for i in range((aa-1)//2-k):
    a=a-A[2*i]-A[2*i+1]+A[2*(i+k)+1]+A[2*(i+k)+2]
    if a>ans:
      ans=a
  print(ans)