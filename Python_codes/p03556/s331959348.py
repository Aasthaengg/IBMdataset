N = int(input())
res = 0
for i in range(32000):
  if i*i > N:
    res = (i-1)*(i-1)
    break
print(res)