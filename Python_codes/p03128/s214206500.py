n,m=map(int,input().split())
A=[int(i) for i in input().split()]
if 2 in A and 3 in A:
  A.remove(2)
if 3 in A and 5 in A:
  A.remove(3)
if 2 in A and 5 in A:
  A.remove(2)
if 6 in A and 9 in A:
  A.remove(6)
m=len(A)
D={}
D[1]=2
D[2]=5
D[3]=5
D[4]=4
D[5]=5
D[6]=6
D[7]=3
D[8]=7
D[9]=6
DP=[-float("inf")]*(n+1)
DP[0]=0
for i in range(n):
  for j in range(m):
    if D[A[j]]<=i+1 and DP[i+1-D[A[j]]]!=float("inf") and DP[i+1-D[A[j]]]+1>=DP[i+1]:
      DP[i+1]=DP[i+1-D[A[j]]]+1
A.sort(reverse=True)
k=DP[n]
ans=""
cur=n
for _ in range(k):
  for j in range(m):
    if cur>=D[A[j]] and DP[cur-D[A[j]]]==DP[cur]-1:
      ans+=str(A[j])
      cur-=D[A[j]]
      break
print(ans)