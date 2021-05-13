from collections import Counter
N = int(input())
X = []
for _ in range(N):
  X.append(list(map(int, input().split())))
  
if N == 1:
  print(1)
  exit(0)
A = []
for i in range(N):
  for j in range(N):
    if i==j:
      continue
    A.append((X[i][0]-X[j][0], X[i][1]-X[j][1]))
    
C = Counter(A)
print(N - C.most_common()[0][1])