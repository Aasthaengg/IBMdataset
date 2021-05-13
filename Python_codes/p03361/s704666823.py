import sys
h,w=map(int,input().split())
l=[]

for i in range(h):
  s=[x for x in input()]
  l.append(s)

for i in range(w):
  im=max(i-1,0)
  ip=min(i+1,w-1)
  for j in range(h):
    jm=max(j-1,0)
    jp=min(j+1,h-1)
    
    if l[j][i]=="#":
      if l[jm][i]=="#" or l[jp][i]=="#" or l[j][ip]=="#" or l[j][im]=="#":
        continue
      else:
        print("No")
        sys.exit()
    else:
      continue
  
print("Yes")