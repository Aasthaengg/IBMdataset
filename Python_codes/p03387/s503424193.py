l=list(map(int,input().split()))
l = sorted(l, reverse=True)
count = 0
while True:
  if l[0] == l[1] == l[2]:
    break
  elif l[0] > l[1]:
    l[1] += 1
    l[2] += 1
  else:
    l[2] += 2
    
  l = sorted(l, reverse=True)
  count += 1
print(count)
