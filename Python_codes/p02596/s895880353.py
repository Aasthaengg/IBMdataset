k = int(input())

x = 0
a = 0
for i in range(1000000):
  x = (pow(10,i,k)*7)%k
  a += x
  if a%k == 0:
    print (i+1)
    exit() 
print (-1)