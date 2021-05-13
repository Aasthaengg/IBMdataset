N = int(input())
A = []

for i in range(1,int(N**0.5)+1):
  if N%i==0:
    A+=[i-1+N//i-1]

print(min(A))