N = int(input())
A = list(map(int,input().split()))
even = 0
odd = 0
for i in range(N):
  if A[i] % 2 == 0:
    even += 1
odd = N - even
if odd % 2 == 0: 
  print('YES')
else:
  print('NO')