n = int(input())

s=0
for i in range(1, n+1):
  if i%15==0:
    pass
  elif i%5==0:
    pass
  elif i%3==0:
    pass
  else:
    s += i
print(s)