N = int(input())
A = list(map(int,input().split()))

## 2個しかない場合
if N == 2:
  A.sort()
  print(A[-1] - A[0])
  print(A[-1], A[0])
  exit()

## 全部非負整数の場合
if sum(a < 0 for a in A) == 0:
  A.sort()
  solver = []
  var = A[0]
  for i in range(1,N-1):
    solver.append((var, A[i]))
    var = var - A[i]
  else:
    solver.append((A[-1], var))
    var = A[-1] - var

  print(var)
  for i in range(len(solver)):
    print(solver[i][0], solver[i][1])
  exit()
  
## 全部非正整数の場合
if sum(a > 0 for a in A) == 0:
  A.sort(reverse=True)
  solver = []
  var = A[0]
  for i in range(1,N):
    solver.append((var, A[i]))
    var = var - A[i]

  print(var)
  for i in range(len(solver)):
    print(solver[i][0], solver[i][1])
  exit()
  
## 正整数も負整数もある場合
A.sort()
n_nega = sum(a < 0 for a in A)
n_posi = sum(a > 0 for a in A)
solver = []
var = A[n_nega-1]
if n_posi > 1:
  for i in range(n_nega,N-1):
    solver.append((var, A[i]))
    var = var - A[i]
solver.append((A[-1], var))
var = A[-1] - var
if n_nega > 1:
  for i in range(n_nega-1):
    solver.append((var, A[i]))
    var = var - A[i]

print(var)
for i in range(len(solver)):
  print(solver[i][0], solver[i][1])


