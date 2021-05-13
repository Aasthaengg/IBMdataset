MM = input().split()
N = int(MM[0])
M = int(MM[1])
C = int(MM[2])
count= 0
BB = input().split()
for i in range(N):
  AA = input().split()
  total = C
  for i,j in zip(BB,AA):
    
    total += int(i)*int(j)
  
  if total >0:
    count +=1
print(count)