n=int(input())


y=[]
for i in range(12):
  y.insert(0,chr(97+(n-1)%26))
  if (n-1)//26>=1:
    n=(n-1)//26
  else:
    break
    

print(''.join(y))