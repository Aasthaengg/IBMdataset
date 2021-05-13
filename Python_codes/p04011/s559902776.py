N=int(input())
K=int(input())
X=int(input())
Y=int(input())

ex=N-K
if ex<0:
  charge=N*X
else:
  charge=K*X+ex*Y

print(charge)