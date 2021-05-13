from collections import Counter
n = int(input())
X = list(map(int, input().split()))
A = Counter(X[::2]).most_common()
B = Counter(X[1::2]).most_common()
A.append((0,0))
B.append((0,0))
if A[0][0]!=B[0][0]:
  print(n-A[0][1]-B[0][1])
else:
  print(min(n-A[0][1]-B[1][1], n-A[1][1]-B[0][1]))