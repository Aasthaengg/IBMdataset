n = int(input())

c = 0
d = 0

for i in range(100):
  for j in range(100):
    if i*4 + j*7 == n:
      print("Yes")
      exit()
print("No")