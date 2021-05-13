n=int(input())
m=round(n/1.08)
if int(m*1.08)==n:
  print(m)
  exit()
else:
  if int((m-1)*1.08)==n:
    print(m-1)
    exit()
  elif int((m+1)*1.08)==n:
    print(m+1)
    exit()
  else:
    print(':(')
    exit()