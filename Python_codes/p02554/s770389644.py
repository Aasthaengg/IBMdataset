n = int(input())
if(n == 1):
  print(0)
elif(n==2):
  print(2)
else:
  print((10**n - 2*9**n + 8**n)%(10**9+7))