A = []
for i in range(5):
  A.append(int(input()))
k = int(input())
if max(A) - min(A) <= k:
  print("Yay!")
else:
  print(":(")