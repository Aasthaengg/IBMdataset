A,B,K=map(int,input().split(' '))

common_divisor=[]
for i in range(100,0,-1):
  if A%i==0 and B%i==0:
    common_divisor.append(i)

print(common_divisor[K-1])