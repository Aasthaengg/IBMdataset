A, V = map(int, input().split(" "))
B, W = map(int, input().split(" "))
T = int(input())

judge = (V-W)*T >= abs(A-B)
if(judge):
  print("YES")
else:
  print("NO")