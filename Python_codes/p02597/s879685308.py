n=int(input())
li=[]
red=0
white=0
count=0
li=list(input())
for i in li:
  if i == 'R':
    red+=1
  else:
    white+=1

checkw=0
for i in range(red):
  if li[i]=='W':
    checkw+=1

checkr=0
for i in range(white):
  if li[i+red]=='R':
    checkr+=1
sa=checkw-checkr
if sa==0:
  print(checkr)
elif sa>0:
  print(checkr+sa)
else:
  print(checkw+sa)