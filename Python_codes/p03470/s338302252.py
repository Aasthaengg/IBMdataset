n=int(input())
li=[]
for i in range(n):
  x=int(input())
  if not x in li:
    li.append(x)
print(len(li))