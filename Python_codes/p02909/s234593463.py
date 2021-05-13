l = ['Sunny','Cloudy','Rainy']
S = input()
p = l.index(S)
if p==0 or p==1:
  print(l[p+1])
else:
  print('Sunny')