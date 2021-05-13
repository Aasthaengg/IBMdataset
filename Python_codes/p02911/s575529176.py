N,K,Q = map(int,input().split())
L = [0 for n in range(N)]

for i in range(Q):
  A = int(input())
  L[A-1] += 1

for j in range(N):
  if K - (Q-L[j]) > 0:
    print("Yes")
  else: 
    print("No")