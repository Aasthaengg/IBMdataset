s=input()
k=0
t=''
u=''
for i in s:
  t+=i
  if not t==u:
    k+=1
    t,u='',t
print(k)