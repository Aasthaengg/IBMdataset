V = []
for i in range(5):
  V.append(int(input()))
               
k = int(input())
               
d = max(V) - min(V)

if d > k:
  print(":(")
else:
  print("Yay!")
