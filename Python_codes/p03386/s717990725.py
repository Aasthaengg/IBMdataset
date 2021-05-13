A,B,K = map(int,input().split())
if B - A < 2*K:
  for i in range(A,B+1):
    print(i)
  exit()
for i in range(K):
    print(A+i)
for i in range(K):
    print(B-K+i+1)