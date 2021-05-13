N, K = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
total = 0
B = [0]*N
for n in range(N):
  count = 0
  for m in range(N):
    if A[m]<A[n]:
      count += 1
  B[n] = count
for n in range(N):
  for m in range(n,N):
    if A[m]<A[n]:
      total+=1
total *= K
K = K*(K-1)//2
for b in B:
  total += b*K
  total %= 1000000007
print(total)