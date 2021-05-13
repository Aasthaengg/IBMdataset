n = int(input())
total = 0
for j in range(1,n+1):
  x = j
  y = n//x
  total +=y*(y+1)*x//2
  
  
print(total)