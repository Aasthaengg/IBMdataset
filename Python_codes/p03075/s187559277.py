A = list()
for _ in range(5):
  A.append(int(input()))
k = int(input())
if A[-1]-A[0]<=k:
  print("Yay!")
else:
  print(":(")