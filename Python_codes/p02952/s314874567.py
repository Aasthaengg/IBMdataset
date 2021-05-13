N = int(input())
res = 0
for i in range(N):
  if  (i+1) // 100000 >= 1:
    pass
  elif (i+1) // 10000 >= 1:
    res +=1
  elif (i+1) // 1000 >= 1:
    pass
  elif (i+1) // 100 >= 1:
    res += 1
  elif (i+1) // 10 >= 1:
    pass
  else:
    res += 1
print(res)