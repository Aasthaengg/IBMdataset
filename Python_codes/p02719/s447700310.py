n,k = map(int,input().split(" "))
a = n%k
b= abs(k-a)
if a <= b:
  print(a)
else:
  print(b)
