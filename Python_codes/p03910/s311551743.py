n=int(input())

i=0
sm=0
while sm<n:
  i+=1
  sm=i*(i+1)//2
d=sm-n
for j in range(1,i+1):
  if j !=d:
    print(j)