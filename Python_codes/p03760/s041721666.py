a,b=input(),input();
length = len(a)+len(b)
result = []
count1 = 0
count2 = 0
for i in range(length):
  if i % 2 == 0:
    try:
      result.append(a[count1])
      count1 += 1
    except:
      continue
  else:
    try:
      result.append(b[count2])
      count2 += 1
    except:
      continue
print(''.join(result))