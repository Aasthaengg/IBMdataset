A,B,K=map(int,input().split())

A,B = min(A,B),max(A,B)

count = 0
for i in range(A,0,-1):
  if A%i==0 and B%i==0:
    count += 1
  if count == K:
    print(i)
    break