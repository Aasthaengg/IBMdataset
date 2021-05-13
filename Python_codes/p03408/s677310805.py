L=list()
R=list()
N=int(input())
for i in range(N):
  S=input()
  L.append(S)
M=int(input())
for i in range(M):
  S=input()
  R.append(S)
maxa=0
for i in range(N):
  s=L.count(L[i])-R.count(L[i])
  maxa=max(maxa,s)
print(maxa)