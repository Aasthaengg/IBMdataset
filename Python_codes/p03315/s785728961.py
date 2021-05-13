a=list(input())
count=0
for i in a:
  if i=='-':
    count-=1
  else:
    count+=1
print(count)