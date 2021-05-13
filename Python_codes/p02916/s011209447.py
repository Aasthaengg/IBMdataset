N = int(input())
A = list(map(lambda a: int(a), input().split(" ")))
B = list(map(lambda b: int(b), input().split(" ")))
C = list(map(lambda c: int(c), input().split(" ")))
 
satis = 0
 
for i in range(len(A)):
  satis += B[A[i] - 1]
  if i >= 1 and A[i] - A[i-1] == 1:
    satis += C[A[i - 1] - 1]
 
print(satis)