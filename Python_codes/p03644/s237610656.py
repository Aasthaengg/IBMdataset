A = int(input())
chek = 1
res = 0
for i in range(10):
  chek = 2**i
  if chek > A:
    res = 2**(i-1)
    break
print(res)