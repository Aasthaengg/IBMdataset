N = int(input())
if N % 2 ==0:
  print(int((N/2)**2))
else:
  print(int(((N-1)/2)*(1+(N-1)/2)))