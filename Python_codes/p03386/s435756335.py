A,B,K=map(int,input().split())
if B-A+1<2*K:
  for i in range(A,B+1):
    print(i)
  exit()
l=list()
for i in range(A,A+K):
  l.append(i)
for i in range(B-K+1,B+1):
  l.append(i)

for i in range(len(l)):
  print(l[i])