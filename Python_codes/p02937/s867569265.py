s=input()
t=input()
ls,lt=len(s),len(t)
if not set(t)<=set(s):print(-1);exit()
co=0
ind=-1
for i in range(lt):
  ind=s.find(t[i],ind+1)
  if ind==-1:
    ind=s.find(t[i])
    co+=1
print(co*ls+ind+1)