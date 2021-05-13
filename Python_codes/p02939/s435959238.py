txt = list(input())
a = txt[0]
count = 1
i = 1
while(i < len(txt)):
  #print(temp)
  if a != txt[i]:
    a = txt[i]
    i += 1
    count += 1
  else:
    if (len(txt)-i) >= 2:
      a = txt[i:i+1]
      i += 2
      count += 1
    else:
      break
print(count)