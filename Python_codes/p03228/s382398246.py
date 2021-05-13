A,B,K=map(int,input().split())
for i in range(K):
  if i%2==0:
    if A%2==0:
      A=A-A//2
      B=B+A
    else:
      A=(A-1)//2
      B=B+A
  else:
    if B%2==0:
      B=B-B//2
      A=B+A
    else:
      B=(B-1)//2
      A=B+A
print(str(A)+" "+str(B))