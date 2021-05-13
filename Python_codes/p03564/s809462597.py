n = int( input())
k = int( input())

a = [1]
b = [1]
x = 10**6
for i in range(n+1):
  for j in range(n-i,n-i+1):
    f = 1*2**i+j*k
    if x > f:
      x = f
      
print(x)