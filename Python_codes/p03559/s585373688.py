from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

AB = [0]*N
sAB = [0]*N
rlt = 0

A.sort()
B.sort()
C.sort()

for i in range(N):
  AB[i] = bisect_left(A, B[i])

sAB[0] = AB[0]
for i in range(N-1):
  sAB[i+1] = sAB[i] + AB[i+1]

for i in range(N):
  j = bisect_left(B, C[i])
  if j == 0:
    continue
  else:
    rlt += sAB[j-1]
  
print(rlt)