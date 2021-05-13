As = list(map(int, input().split()))
K = int(input())

m = 0
max_i = -1
for i,a in enumerate(As):
  if m < a:
    m = a
    max_i = i
    
for i in range(K):
  As[max_i] *= 2
  
print(sum(As))