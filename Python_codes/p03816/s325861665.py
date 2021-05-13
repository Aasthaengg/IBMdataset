N = int(input())
A = [int(i) for i in input().split()]
if len(set(A))%2==0:
  print(len(set(A))-1)
else:
  print(len(set(A)))