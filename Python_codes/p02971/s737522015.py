N = int(input())
A = []
import sys
input = sys.stdin.readline
for i in range(N):
  A.append(int(input().rstrip()))
from collections import Counter
counter = Counter(A)
max_A = max(A)
#B = sorted(set(A), key = A.index)
#B = sorted(B, reverse = True)
#max_A = B[0]
try:
  second_max = sorted(set(A))[-2]
except:
  second_max = max_A
j = False
if counter[max_A] >= 2:
  j = True
for i in range(N):
  if A[i] == max_A and j == False:
    print(second_max)
  else:
    print(max_A)