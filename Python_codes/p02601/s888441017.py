a, b, c = map(int,input().split())
k = int(input())
 
for i in range(k):
  if b <= a:
    b *= 2
  elif c <= b:
    c *= 2
  else:
    break
    
if a >= b or b >= c:
  print('No')
else:
  print('Yes')