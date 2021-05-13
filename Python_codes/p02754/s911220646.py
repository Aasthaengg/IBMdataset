N,A,B = map(int,input().split())
r = N//(A+B)

if N%(A+B)>=A:
  print(r*A+A)

else:
  print(r*A+(N-r*(A+B)))