MM = input().split()
N = int(MM[0])
A = int(MM[1])
B = int(MM[2])
total = 0
for i in range(N+1):
  x = list(str(i))
  total1 = 0
  for j in x:
    
    total1 += int(j)
  
  if A<= total1 <= B:
    total +=i
print(total)