N,L = map(int,input().split())
A = list()
for i in range(N):
  A.append(L+i)
A.sort()
S = sum(A)
if min(A)*max(A)<=0:
  print(S)
else:
  if L>=0:
    print(S-min(A))
  else:
    print(S-max(A))
