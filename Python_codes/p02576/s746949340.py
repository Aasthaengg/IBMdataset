N,X,T = input().split()

N = int(N)
X = int(X)
T = int(T)

if N % X != 0:
  A = ((N // X) + 1 ) * T
else:
  A = (N/X) * T
print(int(A))