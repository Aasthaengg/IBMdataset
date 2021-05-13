N,C=map(int,input().split())
Z=[list(map(int,input().split())) for i in range(N)]
Z.sort()
def judge(x):
  R=[[-1,-1] for i in range(x)]
  for i in range(N):
    for j in range(x):
      if R[j][1]==Z[i][2]:
        R[j][0]=Z[i][1]
        break
      if j==x-1:
        for k in range(x):
          if R[k][0]<Z[i][0]:
            R[k][0]=Z[i][1]
            R[k][1]=Z[i][2]
            break
          if k==x-1:
            return False
  return True

L,R,M=1,C,0
while L!=R:
  M=(L+R)//2
  if judge(M):
    R=M
  else:
    L=max(L+1,M)
print(L)