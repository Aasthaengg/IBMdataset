A,B,K=map(int,input().split())
for i in range(K):
  A//=2
  B+=A
  A,B=B,A
if(K%2):
  A,B=B,A
print(A,B)