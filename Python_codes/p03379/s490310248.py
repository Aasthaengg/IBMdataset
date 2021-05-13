N=int(input())
X=list(map(int,input().split()))
X2=sorted(enumerate(X),key=lambda x:x[1])
X3=sorted(enumerate(X2),key=lambda x:x[1][0])
ans=[0]*N
for i in range(N):
  if X3[i][0] < N//2:print(X2[N//2][1])
  else:print(X2[N//2-1][1])