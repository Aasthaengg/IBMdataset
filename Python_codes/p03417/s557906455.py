n,m = map(int,input().split())
 
if (n == 2 and m != 1) or (m == 2 and n != 1):
  print(0)
elif n ==1 and m != 1:
  print(m-2)
elif m == 1 and n != 1:
  print(n-2)
elif n == 1 and m == 1:
  print(1)
else:
  print(n*m-(n+m-2)*2)
