N, A, B = list(map(int,input().split()))

up = min(A,B)

if A+B >= N:
  down = A+B-N
else:
  down = 0
  
print(up,down)