N=int(input())
A=list(map(int,input().split()))
B=[abs(x) for x in A]
ct=0
for i in range(N):
  if A[i]!=B[i]:
    ct+=1
B.sort()
if B[0]==0 or ct%2==0:
  print(sum(B))
else:
  B[0]*=(-1)
  print(sum(B))