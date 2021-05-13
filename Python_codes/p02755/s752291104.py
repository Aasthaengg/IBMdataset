A,B=map(int,input().split())
c=[]
d=[]
if int(A*100/8)==A*100/8:
  i=int(A*100/8)
else:
  i=int(A*100/8+1)
while i<(A+1)*100/8:
  c.append(i)
  i+=1
if int(B*100/10)==B*100/10:
  j=int(B*100/10)
else:
  j=int(B*100/10+1)
while j<(B+1)*100/10:
  d.append(j)
  j+=1
if min(c[len(c)-1],d[len(d)-1])<max(c[0],d[0]):
  print(-1)
else:
  print(max(c[0],d[0]))