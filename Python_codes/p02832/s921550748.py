N = int(input())
A = input().split(' ')
A = [int(A[i]) for i in range(N)]
NN = 1
count = 0
check = []
for i in range(N):
  if not A[i] == NN:
    count += 1
  else:
    check.append(A[i])
    NN += 1
if not check:
  print(-1)
else:
  print(count)