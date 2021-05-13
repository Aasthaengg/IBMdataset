input1 = list(map(int,input().split()))
K = input1[0]
X = input1[1]
if K * 500 >= X:
  print("Yes")
else:
  print("No")