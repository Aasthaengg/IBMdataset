N = int(input())
A = list(map(int,input().split()))

count = 1
up,down = 1,1

for i in range(1,N):
  if A[i-1] > A[i]:
    up = 0
    if down == 0:
      count += 1
      up,down = 1,1
  elif A[i-1] < A[i]:
    down = 0
    if up == 0:
      count += 1
      up,down = 1,1

print(count)
