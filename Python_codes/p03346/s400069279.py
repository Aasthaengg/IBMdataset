n=int(input())
p=[]
for i in range(n):
  p.append((int(input()),i))
p.sort()
l=-1
s=0
mx=0
for i in range(n):
  if p[i][1]>l:
    s+=1
    mx=max(mx,s)
  else:
    s=1
  l=p[i][1]
print(n-mx)