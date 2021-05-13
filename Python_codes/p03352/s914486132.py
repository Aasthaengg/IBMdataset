X = int(input())
maxi = 0
for i in range(X+1):
  for j in range(2,10):
    
    a = i**j
    
    if a <= X and a > maxi:
      
      maxi = a
print(maxi)