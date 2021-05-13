N,K=map(int,input().split())
R,S,P=map(int,input().split())
T=input()
A=[[] for _ in range(K)]
for i in range(N):
    A[i%K].append(T[i])

count=0
for i in range(K):
  cnt=0
  for j in range(len(A[i])):
    if j==0:
      if A[i][j]=='p':
        count+=S
      if A[i][j]=='s':
        count+=R
      if A[i][j]=='r':
        count+=P
    else:
      if A[i][j]==A[i][j-1]:
        cnt+=1
      if A[i][j]!=A[i][j-1]:
        cnt=0
      if cnt%2==0 and A[i][j]=='p':
          count+=S
      if cnt%2==0 and A[i][j]=='r': 
          count+=P
      if cnt%2==0 and A[i][j]=='s':
          count+=R
print(count)    