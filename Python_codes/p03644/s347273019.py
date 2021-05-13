n = int(input())
a = 1
while True:
  if n < 2 ** a:
    break
  a += 1
print(2**(a-1))