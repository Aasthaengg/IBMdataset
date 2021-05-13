a = [int(input()) for _ in range(5)]
k = int(input())

if a[4] - a[0] <= k:
  print("Yay!")
else:
  print(":(")
