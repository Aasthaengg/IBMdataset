MOD = pow(10,9)+7
N,K = map(int,input().split())
A = list(map(int,input().split()))
L = [[0,0] for _ in range(N)] #leftとright

for i in range(N): #これが基準
  for j in range(N):
    if A[i] > A[j]:
      if i < j:
        L[i][1] += 1
      elif i > j:
        L[i][0] += 1
#print(L)
ans = 0
for i in range(N):
  left = K*(K-1)//2
  right = K*(K+1)//2
  ans = (ans+L[i][0]*left+L[i][1]*right)%MOD
print(ans)
