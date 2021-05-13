N=int(input())
k={}
def y(p):
  if p in k.keys():
    return k[p]
  if p == 0:
    return 2
  elif p == 1:
    return 1
  else:
    k[p] = y(p-2)+y(p-1)
    return k[p]
print(y(N))