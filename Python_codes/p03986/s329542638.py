L=0
R=0
X=list(input())
A=len(X)
for i in range(A):
  if X[i]=="S":
    R=R+1
  elif X[i]=="T":
    if R!=0:
      L=L+1
      R=R-1
print(A-2*L)