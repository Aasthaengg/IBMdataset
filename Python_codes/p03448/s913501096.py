a,b,c,x = map(int,open(0).read().split())

ans = 0 
counta = 0

for i in range(a+1):
  for j in range(b+1):
    for k in range(c+1):
      ans = ((i*500) + (j*100) + (k*50))
      if ans == x:
        counta += 1
      else:
        pass
      
print(counta)
