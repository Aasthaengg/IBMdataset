n = int(input())

if n < 10:
  print(n)

elif n < 10**2:
  print(9)
  
elif n < 10**3:
  print(9+n-100+1)
  
elif n < 10**4:
  print(909)
  
elif n < 10**5:
  print(909+n-10000+1)

else:
  print(90909)