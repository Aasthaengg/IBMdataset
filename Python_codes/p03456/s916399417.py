import math
a, b = input().split()

c = int(a + b)
ans = 'No'
for i in range(math.ceil(math.sqrt(c))+1):
  if i**2 == c: 
    ans = 'Yes'
    break
    
print(ans)

