F =[1,1] + [0 for i in range(44)]

n = int(input())

for i in range(2,n+1):
  F[i]=F[i-1]+F[i-2]

print(F[n])