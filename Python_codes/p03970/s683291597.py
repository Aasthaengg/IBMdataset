s = input()
count = 0
for si,ti in zip(s,"CODEFESTIVAL2016"):
  if si!=ti:
    count+=1
print(count)