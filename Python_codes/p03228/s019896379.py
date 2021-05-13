A, B, K = map(int, input().split())

j, a = A, B
for i in range(K):
  j = j // 2
  a += j 
  j, a = a, j
  
if K % 2 == 0:
  print(j, a)
else:
  print(a, j)