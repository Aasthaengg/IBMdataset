a=input().split()
a=[int(i) for i in a]
b=[]
cnt=0
time=0
for i in range(a[0]):
  b.append(input().split())
  cnt+=int(b[i][1])
i=0
while cnt!=time:
  if int(b[i][1])<=a[1]:
    time+=int(b[i][1])
    print(b[i][0],time)
    b.pop(0)
  else: 
    b[i][1]=int(b[i][1])-a[1]
    time+=a[1]
    b.append(b.pop(i))
    
