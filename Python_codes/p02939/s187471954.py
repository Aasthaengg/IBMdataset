k=0
s=t=''
for c in input():
  s+=c
  if s!=t:
    k+=1
    s,t='',s
print(k)
