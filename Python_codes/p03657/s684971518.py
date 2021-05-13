A,B = map(int,input().split())

flag=0
if A>=3 and A%3==0:
  flag=1
elif B>=3 and B%3==0:
  flag=1
elif (A+B)>=3 and (A+B)%3==0:
  flag=1
  
print('Possible' if flag==1 else 'Impossible')
