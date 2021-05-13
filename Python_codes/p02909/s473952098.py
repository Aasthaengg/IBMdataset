s=input()
wether=['Sunny', 'Cloudy', 'Rainy','Sunny']
for i in range(len(wether)):
  if s==wether[i]:
    print(wether[i+1])
    break