a = [int(input()) for i in range(5)]
k = int(input())
ans = False
for j in range(5):
  for f in range(j+1, 5):
    if a[f] - a[j] > k:
      ans = True
if ans:
  print(":(")
else:
  print("Yay!")