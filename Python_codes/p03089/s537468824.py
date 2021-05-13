n=int(input())
B=list(map(int,input().split()))
A=[]
for i in range(n-1,-1,-1):
  for j in range(i,-1,-1):
    if B[j]==j+1:
      A.append(j+1)
      del B[j]
      break
if len(A)==n:
  for a in A[::-1]:print(a)
else:
  print(-1)