N, K = map(int, input().split())
Aall = [0]*N
count=0
for i in range(K):
  d = int(input())
  A = list(map(int, input().split()))
  for j in range(d):
    Aall[A[j]-1]+= 1
for k in range(N):
  if Aall[k] == 0:
    count+=1
print(count)
