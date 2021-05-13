N,M=list(map(int, input().split()))
A=[list(input()) for _ in range(N)]
B=[list(input()) for _ in range(M)]
K=N-M+1

for i in range(K):
  for j in range(K):
    # print(i,i+M,j,j+M)
    if all(all(A[k+i][l+j] == B[k][l] for l in range(M)) for k in range(M)):
      print('Yes')
      exit()
else:
  print('No')