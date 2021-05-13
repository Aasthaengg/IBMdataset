N,K = map(int, input().split())
A = list(map(int,input().split()))
t = 0
for i in range(N-1):
  for j in range(N-i-1):
    if A[i] > A[j+i+1]:
      t += 1
u = 0
for i in range(N):
  for j in range(N):
    if A[i]>A[j]:
      u += 1
T = t%(10**9+7)
U = u%(10**9+7)
Z=K*(K-1)//2%(10**9+7)
Y=T*K%(10**9+7)
X=U*Z%(10**9+7)
ans = (Y+X)%(10**9+7)
print(ans)