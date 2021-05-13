N=int(input())
X=input()
Y=int(X,2)
Z=Y
C=X.count('1')
if C==1:
  for i in range(N):
    if X[i]=='1':
      print(0)
    elif i==N-1:
      print(2)
    else:
      print(1)
  exit()
Y,Z=Y%(C+1),Z%(C-1)
def f(x):
  if x==0:
    return 0
  return 1+f(x%bin(x).count('1'))
 
for i in range(N):
  if X[i]=='1':
    print(1+f((Z-pow(2,N-i-1,C-1))%(C-1)))
  else:
    print(1+f((Y+pow(2,N-i-1,C+1))%(C+1)))
