N = int(input())
A = [0]+list(map(int,input().split()))
A.sort()
B = [0]+list(map(int,input().split()))
B.sort()
C = [0]+list(map(int,input().split()))
C.sort()

bko = [0 for i in range(N+1)]
cnt = 1
for i in range(1,N+1):
  b = B[i]
  for j in range(cnt,N+1):
    if A[j] >= b:
      bko[i] = j-1
      cnt = j
      break
    if j == N:
      bko[i] = N
      cnt = N

#bkoを累積和にする
for i in range(N):     
  bko[i+1] += bko[i]

cko = [0 for i in range(N+1)]
cnt = 1
for i in range(1,N+1):
  c = C[i]
  for j in range(cnt,N+1):
    if B[j] >= c:
      cko[i] = bko[j-1]
      cnt = j
      break
    if j == N:
      cko[i] = bko[N]
      cnt = N
###
print(sum(cko))        