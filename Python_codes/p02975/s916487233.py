n = int(input())

A = list(map(int,input().split()))
from collections import Counter

for a in A:
  if a != 0:
    break
else:
  print('Yes')
  exit()

A = list(Counter(A).most_common())

if len(A) == 2 and A[1][0]==0 and A[1][1] == n//3:
  print('Yes')
  exit()

B = []
for a,c in A:
  if c != n//3:
    print('No')
    exit()
  B.append(a)
n = len(str(max(B)))
  
B = [[(1<<j&i)>>j for j in range(30)] for i in B]
for i in range(30):
  if B[0][i]^B[1][i]^B[2][i] != 0:
    print('No')
    break
else:
  print('Yes')