s=input()
 
ds=list(s)
 
 
c1=0
while ds[c1]!='A':
  c1+=1
 
c2=-1
while ds[c2]!='Z':
  c2-=1
 
print(len(s[c1:c2])+1)