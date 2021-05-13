A,B,K=map(int,input().split())
while True:
  A-=A%2
  A,B=A//2,B+A//2
  K-=1
  if K==0:
    break
  B-=B%2
  B,A=B//2,A+B//2
  K-=1
  if K==0:
    break
print(A,B)