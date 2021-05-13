x,y=map(int,input().split())
               
iimax=int(18/3*10+1)        

m=y//x

i2=1
for i in range(iimax):
  if m<2*i2:
      print(i+1)
      break
  else :
      i2=i2*2
      
