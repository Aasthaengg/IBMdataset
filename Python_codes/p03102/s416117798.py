h, m, c = map(int, input().split())
b = list(map(int, input().split()))

count = 0
for i in range(h):
  ans = 0
  a = list(map(int, input().split()))
  
  for j in range(m):
    ans = ans + a[j]*b[j]
  ans = ans + c
    
  if ans > 0:
    count += 1
print(count)