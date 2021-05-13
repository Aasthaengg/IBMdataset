s=list(input())
ls=len(s)
r=[0]*ls
c=0
for ii in range(ls-1):
  if s[ii]=="R" and s[ii+1]=="R":
    c+=1
  elif s[ii]=="R" and s[ii+1]=="L":
    c+=1
    r[ii]+=c//2+c%2
    r[ii+1]+=c//2
    c=0
  elif s[ii]=="L" and s[ii+1]=="L":
    pass
  elif s[ii]=="L" and s[ii+1]=="R":
    pass
  #print(c)
#print(*r)
c=0  
for jj in range(ls-1):
  ii=ls-1-jj
  if s[ii-1]=="R" and s[ii]=="R":
    pass
  elif s[ii-1]=="R" and s[ii]=="L":
    c+=1
    r[ii-1]+=c//2
    r[ii]+=c//2+c%2
    c=0
  elif s[ii-1]=="L" and s[ii]=="L":
    c+=1
  elif s[ii-1]=="L" and s[ii]=="R":
    pass
  #print(ii,c)
print(*r)