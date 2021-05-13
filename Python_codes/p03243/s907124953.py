N = int(input())
f = 0
for i in range(1, 10):
  if N <= i * 111:
    print(i * 111)
    f = 1
    break
if f == 0:
  print(1111)