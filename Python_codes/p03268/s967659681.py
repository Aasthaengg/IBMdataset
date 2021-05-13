N,K=[int(x) for x in input().split()]
if K%2:
  mod0=N//K
  print(mod0**3)
else:
  mod0,MODN=divmod(N,K)
  if MODN>=K//2:
    print(mod0**3+(mod0+1)**3)
  else:
    print((mod0**3)*2)