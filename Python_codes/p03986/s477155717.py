x=input()
s,a=0,0
for i in x:
 if i=="S":
  s+=1
 elif s==0:
  a+=1
 else:
  s-=1
print(a+s)