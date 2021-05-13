A = int(input())
B = int(input())
C = int(input())
X = int(input())

count=0
tot = 0
for i in range(A+1):
  for j in range(B+1):
    tot = i*500 + j*100
    
    if (X-tot)%50==0 and C>=(X-tot)//50>=0:
      count+=1
      
print(count)