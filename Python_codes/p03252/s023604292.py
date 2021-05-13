s=input()
t=input()

t1=0
l1={}
sl=[]
for i in s:
  if i in l1:
    sl.append(l1[i])
  else:
    l1[i]=t1
    sl.append(t1)
    t1+=1

t2=0
l2={}
tl=[]
for i in t:
  if i in l2:
    tl.append(l2[i])
  else:
    l2[i]=t2
    tl.append(t2)
    t2+=1
print("Yes" if sl==tl else "No")