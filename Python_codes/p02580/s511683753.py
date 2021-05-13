h,w,m=map(int,input().split())
d_h=[0]*(h+1)
d_w=[0]*(w+1)
d=[]
for i in range(m):
  nh,nw=map(int,input().split())
  d_h[nh]+=1
  d_w[nw]+=1
  d.append([nh,nw])
  
#print(d_h)
#print(d_w)

hantei=0
ans1=max(d_h)
memoh=set()
for i in range(1,h+1):
  hantei=d_h[i]
  if ans1==hantei:
    memoh.add(i)
    
hantei=0
ans2=max(d_w)
memow=set()
for j in range(1,w+1):
  hantei=d_w[j]
  if ans2 == hantei:
    memow.add(j)
ans = ans2+ans1-1
#print(memoh,memow)
count = len(memoh)*len(memow)
for hw in d:
  if hw[0] in memoh and hw[1] in memow:
    count-=1
if count>0:
  print(ans+1)
else:
  print(ans)
