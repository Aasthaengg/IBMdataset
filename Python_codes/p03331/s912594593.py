N=int(input())
if N==10 or N==10**2 or N==10**3 or N==10**4 or N==10**5:
  print(10)
else:
  a=list(str(N))
  b=sum([int(i) for i in a])
  print(b)
