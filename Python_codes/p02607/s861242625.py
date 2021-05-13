N = int(input())
A = [int(x) for x in input().split()]

C = 0
for i in range(0,N,2):
  if A[i] % 2 == 1:
  	C += 1
    
print(C)