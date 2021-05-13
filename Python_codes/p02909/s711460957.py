a=input()
b=['Sunny','Cloudy','Rainy']
for i in range(3):
  if i==2:
    print('Sunny')
    break
  if b[i]==a :
    print(b[i+1])
    break