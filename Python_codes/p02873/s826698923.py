s=input()
 
sl=len(s)+1
l=[0]*sl
 
for i in range(sl-1):
  if s[i]=="<":
    l[i+1]=l[i]+1
    
for i in range(sl-2,-1,-1):
  if s[i]==">":
    l[i]=max(l[i+1]+1, l[i])
    
print(sum(l))