found = dict()
def getsums(n):
  if n==0:return 1
  elif n<3:return 0
  elif n==3:return 1
  num = 0
  for x in range(3,n+1):
    if n-x in found:
      num+=found[n-x]
    else:
      g = getsums(n-x)
      found[n-x]=g
      num+=g
  return num

print(getsums(int(input()))%((10**9)+7))