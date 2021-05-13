N = int(input())
D, X = map(int, input().split())
A = [int(input()) for i in range(N)]

total = 0

for i in range(N):
  day = 1
  while 1:
    if day > D:
      break
    else:
      total += 1
      day += A[i]
else:
  print(X + total)