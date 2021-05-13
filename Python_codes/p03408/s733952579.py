blue=int(input())
b=[]
r=[]
for i in range(blue):
  b.append(input())
red=int(input())
for i in range(red):
  r.append(input())
count=[]
for i in range(len(b)):
  counter=0
  for j in range(len(b)):
    if b[i]==b[j]:
      counter+=1
  for j in range(len(r)):
    if b[i]==r[j]:
      counter-=1
  count.append(counter)
if max(count)<0:
  print(0)
else:
  print(max(count))