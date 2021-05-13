n=int(input())
li=[]
for i in range(n):
  li.append(int(input()))
out=sum(li)
if out%10!=0:
  print(out)
else:
  li.sort()
  for i in li:
    if i%10!=0:
      print(out-i)
      break
  else:
    print(0)