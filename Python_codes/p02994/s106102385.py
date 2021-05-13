N, L = map(int, input().split())
s = 0
min = 10**9
for i in range(N):
  s = s + i + L 
  if min > abs(i+L):
    min = abs(i+L)

if s > 0:
  print(s-min)
else:
  print(s+min)