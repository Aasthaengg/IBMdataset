N=int(input())
a=0
b=[0]
for i in range(N):
  tmp=int(input())
  if tmp%10!=0:
    b.append(tmp)
  a+=tmp
b.sort()
if a%10!=0:
  print(a)
else:
  if len(b)!=1:
    print(a-b[1])
  else:
    print(0)