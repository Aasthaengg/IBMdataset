A,B,K=map(int,input().split())

for i in range(K):
  if i%2==0:
    A=A-A%2
    A,B=A-A//2,B+A//2
  else:
    B=B-B%2
    A,B=A+B//2,B-B//2
  #print(A,B)
print(A,B)