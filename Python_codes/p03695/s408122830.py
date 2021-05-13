N = int(input())
A = list(map(int, input().split()))
ans = [0] * 9

for i in range(N):
  aa = int(A[i] / 400)
  if aa > 8:
    aa = 8
  ans[aa] += 1
  
min_a = 0
max_a = 0
for i in range(9):
  if i != 8:
    if ans[i] != 0:
      min_a += 1
      max_a += 1
  else:
    max_a += ans[i]
    
min_a = max(min_a, 1)    
print(min_a, max_a)



