n=int(input())
if n//100<(n%100)//10 or (n//100==(n%100)//10 and n//100<(n%10)):
  print(((n//100)+1)*111)
else:
  print((n//100)*111)