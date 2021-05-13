N,M,X=list(map(int, input().split()))
L=list(map(int, input().split()))
c=0
d=0
for i in range(M):
  if L[i]>X:
    c+=1
  else:
    d+=1
print(min(c,d))
