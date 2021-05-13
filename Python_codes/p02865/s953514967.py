n=int(input())
if n==1:
  print(0)
for i in range(1,n):
  if n-i<=i:
    print(i-1)
    break