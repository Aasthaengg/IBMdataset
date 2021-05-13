N=int(input())
t=2*N
i=1
while i*i<=N:
  if N%i==0:
    if (i-1)+(N//i-1)<=t:
      t=(i-1)+(N//i-1)
  i += 1
print(t)
