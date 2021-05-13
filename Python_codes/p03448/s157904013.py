A = int(input())
B = int(input())
C = int(input())
X = int(input())
a = X // 500
b = (X - 500*a) // 100
c = (X - 500*a - 100*b) //50 

count = 0
i = a 
while i >= 0:
  j = b
  k = c
  while j >= 0:
    if i <= A and j <= B and k <= C:
      count += 1 
    j -= 1
    k += 2
  i -= 1
  b += 5
  
print(count)