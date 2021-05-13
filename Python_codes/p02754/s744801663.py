N,A,B = map(int,input().split())

n = N%(A+B)

if n <= A:
  print(N//(A+B)*A + n)
else:
  print(N//(A+B)*A + A)