x=int(input())
temp=0
for i in range(1,x+1):
  temp=temp+i
  if temp>=x:
    break
print(i)