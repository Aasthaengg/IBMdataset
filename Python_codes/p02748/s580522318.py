A,B,M = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
min = min(A)+min(B)
for i in range(M):
  x,y,c = [int(i) for i in input().split()]
  buf = A[x-1]+B[y-1]-c
  if buf<min:
    min = buf
print(min)