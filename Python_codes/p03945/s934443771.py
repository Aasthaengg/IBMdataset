s=str(input())
sl=list(s)
count=0
for i in range(0,len(sl)-1):
  if sl[i]!=sl[i+1]:
    count=count+1
print(count)