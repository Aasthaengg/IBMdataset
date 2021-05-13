N=int(input())
K=int(input())
x=int(input())
y=int(input())

if N>K:
  s=x*K+y*(N-K)
else:
  s=x*N
print(int(s))