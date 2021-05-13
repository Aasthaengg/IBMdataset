import math
N = int(input())
A = [0]
A.extend(list(map(int, input().split())))
A.append(0)

hoge = sum([abs(A[i] - A[i-1]) for i in range(1, N+2)])

for i in range(1, N+1):
  print(hoge + abs(A[i-1] - A[i+1]) - (abs(A[i-1] - A[i]) + abs(A[i] - A[i+1])))
 
