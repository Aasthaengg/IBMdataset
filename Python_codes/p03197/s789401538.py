N = int(input())
A = [int(input()) for _ in range(N)]
if len([0 for a in A if a % 2 == 0]) == N:
  print('second')
else:
  print('first')