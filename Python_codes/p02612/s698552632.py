n=int(input())
if n%1000!=0:
  print(abs(int(n%1000)-1000))
else:
  print(n%1000)
