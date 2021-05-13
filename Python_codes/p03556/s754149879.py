a=int(input())
k=1
for i in range(0,100000):
  if a<(k**2):
    break
  else:
    k+=1
print((k-1)**2)
