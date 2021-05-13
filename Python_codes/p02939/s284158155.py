s=input()
count=1
ps=s[0]
i=1
while i<len(s):
  if s[i]!=ps:
    count+=1
    ps=s[i]
    i+=1
  elif i==len(s)-1:
    break
  else:
    count+=1
    ps=s[i:i+2]
    i+=2
print(count)