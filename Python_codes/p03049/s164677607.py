n = int(input())
s = [input() for i in range(n)]
count,a,b,ab = 0,0,0,0
for word in s:
  count += word.count("AB")
  if word[0] == "B" and word[-1] =="A":
    ab += 1
  elif word[0] == "B":
    b += 1
  elif word[-1] == "A":
    a += 1
  else:
    pass
if ab == 0:
  print(min([a,b])+count)
else:
  if a == 0 and b == 0:
    print(ab-1+count)
  elif a == 0 or b == 0:
    print(ab+count)
  else:
    print(ab+1+min([a-1,b-1])+count)
