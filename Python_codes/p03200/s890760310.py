s=input()
bl=[]
wl=[]
for j,si in enumerate(s):
  if si=="B":
    bl.append(j)
  else:
    wl.append(j)

blen=len(bl)
wlen=len(wl)

ans=0
for i,j in zip(wl,range(wlen)):
  ans+=abs(i-j)
  
print(ans)



