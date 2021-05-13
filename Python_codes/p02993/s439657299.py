a=list(input())
count=0

       
for i in range(4):
  if i==3:
    break
  if a[i]==a[i+1] :
    count+=1
if count>=1:
  print('Bad')
else:
  print('Good')