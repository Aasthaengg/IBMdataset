n = int(input())
k = int(input())

i = 0
m = 1
while True:
  if m < k:
    m = m*2
    i += 1
  else:
    break
    
if i <= n :
  print(2**i + k * (n-i))
else :
  print(2**n)