N=int(input())
print(0)
a=input()
m=-1
if a=="Vacant":
  exit()
elif a=="Male":
  m=0
elif a=="Female":
  m=1
l,r=1,N-1
while r-l>1:
  mid=(l+r)//2
  print(mid)
  a=input()
  if a=="Vacant":
    exit()
  elif a=="Male" and (mid-m)%2==0:
    l=mid
  elif a=="Female" and (mid-m)%2==1:
    l=mid
  else:
    r=mid
print(l)
if input()=="Vacant":
  exit()
print(r)
if input()=="Vacant":
  exit()
