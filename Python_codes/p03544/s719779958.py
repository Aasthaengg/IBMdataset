

def luca(n):
  lz=2
  lo=1
  if n==1:
    return 1
  for i in range(n-1):
    
    nl=lz+lo
    lz=lo
    lo=nl

  return nl

print(luca(int(input())))
