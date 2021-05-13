N = int(input())
A =list(map(int, input().split()))


odd = 0

for i in range(N):
  if A[i] % 2 !=0:
    odd += 1
    
    
if odd % 2 !=0 :
  print('NO')
else:
  print('YES')