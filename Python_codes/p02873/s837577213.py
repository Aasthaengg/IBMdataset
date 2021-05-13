s=input()
l=[]
i=0
while i<len(s):
  k=0
  while s[i]=='<' if i<len(s) else False:
    k+=1
    i+=1
  if k>0:
    l.append(k)
  k=0
  while s[i]=='>' if i<len(s) else False:
    k+=1
    i+=1
  if k>0:
    l.append(k)
sm=0
for i in l:
  sm+=(i*(i+1))//2
for i in range(0 if s[0]=='<' else 1,len(l)-1,2):
  sm-=min(l[i],l[i+1])
 
  
print(sm)