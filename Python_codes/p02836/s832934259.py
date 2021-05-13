ess = input()
sse = ess[::-1]
hugs = 0
for i in range(0, len(ess)):
  if ess[i] != sse[i]: hugs += 1
    
print(int(hugs/2))
