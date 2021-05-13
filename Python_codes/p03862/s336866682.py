N,X,*A = map(int,open(0).read().split())
A+=[0]
s = 0

for n in range(N):
  d=max(0,A[n]+A[n-1]-X)
  s+=d
  A[n]-=d

print(s)