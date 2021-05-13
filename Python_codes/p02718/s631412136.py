N, M=map(int, input().split())
A=[int(x) for x in input().split()]
A.sort()
S=sum(A)
if A[N-M]*(4*M)>=S:
  print("Yes")
else: print("No")

