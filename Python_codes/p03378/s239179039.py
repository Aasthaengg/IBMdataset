N,M,X = map(int,input().split())
A = list(map(int,input().split()))

cnt = 0
for i in range(M):
  if A[i] < X:
    cnt += 1
  else:
    break
print(min(cnt,M - cnt))