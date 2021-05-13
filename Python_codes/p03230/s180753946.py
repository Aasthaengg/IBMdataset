n=int(input())
if int((2*n)**(0.5))*int((2*n)**(0.5)+1)==2*n:
  print('Yes')
  k=int((2*n)**(0.5)+1)
  print(k)
  l=[]
  for i in range(k):
    if i==0:l.append([j+1 for j in range(k-1)]);lused=k-1
    else:
      addl=[]
      for j in range(i):
        addl.append(l[j][i-1])
      for j in range((k-1)-i):
        addl.append(lused+1)
        lused+=1
      l.append(addl)
  for i in l:print(2*n//k,*i)
else:print("No")