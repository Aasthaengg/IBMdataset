k,s = map(int, input().split())

l = 0

if s <= k:
  l = int((s+2)*(s+1)/2)
else:
  for x in range(0,k+1):
    if s-x > 2*k:
      l += 0
    elif k < s-x <= 2*k:
      l += 2*k - s + x + 1
    elif s-x <= k:
      l += s-x+1      
print(l)
