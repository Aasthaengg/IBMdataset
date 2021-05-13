input1 = list(map(int,input().split()))
A = input1[0]
B = input1[1]
C = input1[2]
D = input1[3]
if A * B >= C * D:
  print(A * B)
else:
  print(C * D)