s = input()
count =0
fcount = 0
for i in s:
  if i=='R' and count>0:
    count = count + 1
    fcount = max(fcount,count)
  elif i=='R':
    count = 1
    fcount = 1
  else:
  	count = 0
print(fcount)
