a = [int(input()) for i in range(5)]
k = int(input())
for i in a:
  for j in a:
    if j-i > k:
      print(":(")
      exit()
print("Yay!")