from itertools import accumulate

N = int(input())
A = list(map(int,input().split()))
A = sorted(A)
S = list(accumulate(A))
AS = []
flg = False
count = 0

for i in range(N-1):
  AS.append(S[i]*2 - A[i+1])
for j in range(N-2,-1,-1):
  if AS[j] < 0:
    count = j+1
    break
print(len(A)-count)