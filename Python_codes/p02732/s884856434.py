import collections
import math

N = int(input())
A = list(map(int, input().split()))
c = collections.Counter(A)
answer = 0
for num in c:
  answer += c[num]*(c[num]-1)//2

for k in range(N):
  print(answer - c[A[k]] + 1)