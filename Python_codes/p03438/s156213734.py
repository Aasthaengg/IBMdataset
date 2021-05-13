N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

plus, minus = 0, 0
for i in range(N):
  if a[i]-b[i] >= 0:
    minus += a[i]-b[i]
  else:
    m = b[i]-a[i]
    plus += (m+1) // 2
    if m%2 == 1:
      minus += 1
    
if plus >= minus:
  print('Yes')
else:
  print('No')