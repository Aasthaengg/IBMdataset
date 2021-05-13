t,s=0,0
for x in input():
 if x=='S':s+=1
 elif s:s-=1
 else:t+=1
print(t+s)