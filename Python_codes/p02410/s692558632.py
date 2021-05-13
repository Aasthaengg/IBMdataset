n, m = map(int, raw_input().split())
A = []
b = []
    
for i in range(0, n):
   A += [map(int, raw_input().split())]
  
for j in range(0, m):
   b += [input()]
     
for i in range(0, n):
   c = 0
   for j in range(0, m):
      c += A[i][j] * b[j]
   print c