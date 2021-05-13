blue=int(input())
b=[]
r=[]
count=[]
for i in range(blue):
  b.append(input())
red=int(input())
for i in range(red):
  r.append(input())
for i in b:
  count.append(b.count(i)-r.count(i))
if max(count)<0:
  print(0)
else:
  print(max(count))