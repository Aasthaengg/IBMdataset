N = int(input())
A = []
B = []
for _ in range(N):
  a,b = [int(i) for i in input().split()]
  A.append(a)
  B.append(b)
A.sort()
B.sort()
if N%2 == 1:
  M = (N-1)//2
  print(B[M]-A[M]+1)
  exit()
M = (N//2)-1
L = (N//2)
print(B[M]+B[L]-A[M]-A[L]+1)