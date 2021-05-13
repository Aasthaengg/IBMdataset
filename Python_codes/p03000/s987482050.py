n,x = map(int, input().split())
L = list(map(int, input().split()))

H = 0
count = 0
for i in range(n):
  if H > x:
    print(count)
    exit()
  else:
    H += L[i]
    count += 1
  
if H > x:
  print(n)
else:
  print(n+1)