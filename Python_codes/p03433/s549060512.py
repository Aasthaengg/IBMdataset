N = int(input())
A = int(input())
n5 = int(N/500)
a = N - n5 * 500
if a <= A:
  print("Yes")
else:
  print("No")