N, M=map(int,input().split())
H=list(map(int,input().split()))
ans=[1]*N
for i in range(M):
  A, B=map(int, input().split())
  if H[A-1]>H[B-1]:
    ans[B-1]=0
  elif H[B-1]>H[A-1]:
    ans[A-1]=0
  elif H[A-1]==H[B-1]:
    ans[A-1]=0
    ans[B-1]=0
print(sum(ans))
