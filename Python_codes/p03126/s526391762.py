N,M=map(int,input().split())
n = [0]*(M+1)
for i in range(N):
  K,*A=map(int,input().split())
  for j in range(K):
    n[A[j]] += 1

count = 0
for i in range(len(n)):
  if n[i]==N:count += 1

print(count)