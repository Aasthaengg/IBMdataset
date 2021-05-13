N=int(input())
min=10*N
for A in range(1,N):
  B=N-A
  sum=0
  while A>0:
    sum+=A%10
    A=A//10
  while B>0:
    sum+=B%10
    B=B//10
  if min>sum:
    min=sum
print(min)