N, K = map(int, input().split())
c = 0
for i in range(1,N+1):
    b = i*K
    if b <= N:
      c += 1
    else:
      break
e = 0
if K%2 ==0:
  for i in range(1,N+1):
    d = i*K/2
    if d <= N and d%K != 0:
      e += 1 
  print(c**3 + e**3)
else:
  print(c**3)