N,M=map(int,input().split())
A=[input() for _ in range(N)]
B=[input() for _ in range(M)]
for i in range(N-M+1):
  for j in range(len(A[i])-len(B[0])+1):
    if B[0][0]==A[i][j]:
      flag=True
      p=i
      for k in range(M):
        if not B[k]==A[p][j:j+len(B[k])]:
          flag=False
          break
        p+=1
      if flag:
        print('Yes')
        exit()
print('No')