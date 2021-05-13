N = int(input())
res = 0
for x in range(1,N+1):
  x = str(x)
  if len(x) % 2 == 1:
    res += 1
print(res)