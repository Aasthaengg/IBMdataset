n,x=map(int,input().split())
l=sorted(list(map(int,input().split())))

c=0
for i in l:
  x-=i
  if x<0:
    c+=1
    break
  else:
    c+=1

if x!=0:
  c-=1


print(c)