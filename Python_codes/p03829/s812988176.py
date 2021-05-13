n, a, b = map(int, input().split())
x = list(map(int, input().split()))

res = 0
for i in range(n-1):
  tmp = a * (x[i+1] - x[i])
  if tmp > b:
    res += b
  else:
    res += tmp
    
print(res)