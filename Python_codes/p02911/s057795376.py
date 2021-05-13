N,K,Q = map(int,input().split())
P = N*[K-Q]

for q in range(Q):
  a = int(input())
  P[a-1]+=1

for n in range(N):
  if P[n]<=0:
    print("No")
  else:
    print("Yes")