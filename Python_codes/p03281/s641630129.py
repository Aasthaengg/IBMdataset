N = int(input())

y = 0
def X(num):
  x = 0
  for i in range(1,num+1):
    if num%i == 0:
      x += 1
  return x
for j in range(1,N+1):
  if X(j) == 8 and j%2==1:
    y = y+1
print(y)