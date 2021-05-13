X=int(input())
a=[]
for i in range(-100,200):
  for j in range(-100,200):
    if i**5-j**5==X:
      a.append(str(i))
      a.append(str(j))
      break
  else:
    continue
  break  
print(' '.join(a[0:2]))

    
