N = input()

W = ['Sunny','Cloudy','Rainy']

for i in range(3):
  if N == 'Rainy':
    print('Sunny')
    break
  elif N == W[i]:
    print(W[i+1])
  else:
    pass
  i+=1
