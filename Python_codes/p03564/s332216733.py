n= int(input())
k = int(input())
z = 1
for i in range(n):
  if z < k:
    z = 2*z
  else:
    z = z+k
print(z)