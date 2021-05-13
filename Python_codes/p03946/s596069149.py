N,T = map(int,input().split())
A = list(map(int,input().split()))
minA = [[A[0],0]] + [[-1,-1]]*(N-1)
for i in range(1,N):
  if minA[i-1][0] >= A[i]: minA[i] = [A[i],i]
  else: minA[i] = minA[i-1]
  
maxA = [[-1,-1]]*(N-1) + [[A[-1],N-1]]
for i in range(N-2,-1,-1):
  if maxA[i][0] <= A[i]: maxA[i] = [A[i],i]
  else: maxA[i] = maxA[i-1]

max_dif = -float('inf')
max_i = []
cnt = 0
for mina, maxa in zip(minA, maxA):
  if max_dif < maxa[0]-mina[0]:
    max_dif = maxa[0]-mina[0]
    max_i = [cnt]
  elif  max_dif == maxa[0]-mina[0]:
    max_i.append(cnt)
  cnt += 1

print(len(max_i))