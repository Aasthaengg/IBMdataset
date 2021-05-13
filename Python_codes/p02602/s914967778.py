N,K = map(int, input().split())
A = list(map(int,input().split()))

idx = K-1

while(idx < N-1):
  idx += 1
  if A[idx] / A[idx-K] > 1:
    print("Yes")
  else:
    print("No")