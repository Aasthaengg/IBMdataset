h,w,k,*S=open(0).read().split()
h,w=int(h),int(w)
c,n=0,0
for s in S:
  l,r=-1,s.find('#')
  n+=1
  if r==-1:continue
  t=[]
  while r!=-1:
    c+=1
    t+=[c]*(r-l)
    l,r=r,s.find('#',r+1)
  t+=[c]*(w-l-1)
  for i in range(n):
    print(*t)
  n=0
for i in range(n):
  print(*t)