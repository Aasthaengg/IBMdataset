n=int(input())
b=list(map(int,input().split()))
i=0
c=[]
while len(b)>0 and i<len(b):
  if b[len(b)-i-1]==len(b)-i:
    c.append(len(b)-i)
    b.remove(b[len(b)-i-1])
    i=0
  else:
    i+=1
if len(b)==0:
  for i in range(n):
    print(c[n-i-1])
else:
  print(-1)