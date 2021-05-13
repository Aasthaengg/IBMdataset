N=int(input())
A=list(map(int,input().split()))
B=[]
for i in range(N):
  for j in range(len(A)-1,-1,-1):
    if A[j]==j+1:
      B.append(A.pop(j))
      break
  else:
    print(-1)
    exit()

for i in B[::-1]:
  print(i)