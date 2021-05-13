N,*A = map(int,open(0).read().split())
A.sort()
B = [[] for i in range(100)]
B[0]= A
#print(B)
for i in range(99):
  B[i+1].append(B[i][0])
  for j in range(1,len(B[i])):
    x = B[i][j]%B[i][0]
    if x!=0:
      B[i+1].append(x)
  B[i+1]=sorted(B[i+1])
  if len(B[i])<=1:
    break
print(B[i][0])