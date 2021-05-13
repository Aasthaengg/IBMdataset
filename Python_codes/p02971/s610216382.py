n=int(input())
A=[int(input()) for i in range(n)]
ma=max(A)
flag=False
if A.count(ma)>=2:
  flag=True
for i in range(n):
  if A[i] != ma:
    print(ma)
  else:
    if flag:
      print(ma)
    else:
      A[i]=0
      print(max(A))