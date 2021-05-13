X = int(input())

ans = X
m = int(X ** .5)
t = m * (m + 1) // 2
while True:
  if X <= t:
    break
    
  m += 1
  t = m * (m + 1) // 2

print(m)
