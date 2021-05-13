n = int(input())
A = list(map(int,input().split()))
MaxA = max(A)
A = sorted(A,key=lambda x: abs(MaxA/2-x))
if A[0] == MaxA:
  print(MaxA,A[1])
else:
  print(MaxA,A[0])