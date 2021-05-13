V = input()
N,X,T = V.split()
N = int(N)
X = int(X)
T = int(T)
if(N%X==0):
  c = N/X
else:
  c = N//X + 1
  
A = int(c*T)
  
print(A)