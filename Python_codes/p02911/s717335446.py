N,K,Q = map(int,input().split())
A = [int(input()) for q in range(Q)]
P = N*[K-Q]

for a in A:
  P[a-1]+=1

for n in range(N):
  if P[n]<=0:
    print("No")
  else:
    print("Yes")