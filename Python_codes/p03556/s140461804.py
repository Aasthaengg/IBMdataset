n = int(input())
 
a = 1
b = 0
c = 0

 
while c <= n:
  b = c
  c = a ** 2
  a += 1
  
print(b)