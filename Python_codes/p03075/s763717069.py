A = []
for i in range(5):
  a = int(input())
  A.append(a)
k = int(input())  
for i in range(5):
  for j in range(i,5):
    if A[j] -A[i] <= k:
      pass
    else:
      print(":(")
      quit()
print("Yay!")