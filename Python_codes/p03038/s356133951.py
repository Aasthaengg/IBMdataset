N,M=map(int,input().split())
A=list(map(int,input().split()))
A.sort()
B=[list(map(int,input().split())) for _ in range(M)]
B.sort(key=lambda x:-x[1])
i,j=0,0
while i<=N-1:
  for l in range(B[j][0]):
    if A[i]>=B[j][1]:
      print(sum(A))
      exit()
    A[i]=B[j][1]
    i+=1
    if i==N:
      print(sum(A))
      exit()
  j+=1
  if j==M:
    print(sum(A))
    exit()
print(sum(A))