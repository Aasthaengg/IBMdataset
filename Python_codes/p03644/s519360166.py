n = int(input())
a=0
for i in range(10):
  x = 2 ** i
  if x <=n:
    a=x
    
print(a)