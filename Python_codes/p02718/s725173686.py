N,M = map(int,input().split())
A = list(map(int,input().split()))
T = sum(A)/(4*M)

if M<=sum(T<=a for a in A):
  print("Yes")
else:
  print("No")