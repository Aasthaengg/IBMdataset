import copy
N=int(input())
X=list(map(int,input().split()))
B=[]
P=copy.copy(X)
X.sort()
a=X[N//2-1]
b=X[N//2]
for i in range(N):
  if P[i]<=a:
    B.append(b)
  else:
    B.append(a)
for j in range(N):
  print(B[j])