K, S = [int(a) for a in input().split()]

cnt = 0
for x in range(0,K+1):
  if x > S:
    continue
  for y in range(0,K+1):
    if x+y > S:
      continue
    elif x+y+K < S:
      continue
    else:
      cnt +=1
        
print(cnt)