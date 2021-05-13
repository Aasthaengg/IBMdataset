A,B,K=map(int,input().split())
if A==B:
  print(A)
  exit()
if B-A<K:
  K=B-A
l=list()
for i in range(A,A+K):
  l.append(i)
for i in range(B-K+1,B+1):
  l.append(i)
l=set(l)
l=sorted(l)
for i in range(len(l)):
  print(l[i])