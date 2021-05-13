N=int(input())
A=list(map(int, input().split()))
A.sort()
P=sum([1 for a in A if a >= 0])
Q=N-P
if P==0:
  P=1
  Q=N-1
elif Q==0:
  P=N-1
  Q=1
ans=[]
for y in range(Q, N-1):
  ans.append((A[0], A[y]))
  A[0]=A[0]-A[y]

for y in range(Q):
  ans.append((A[N-1],A[y]))
  A[N-1]=A[N-1]-A[y]

print(A[N-1])
for x in ans:
  print(*x)