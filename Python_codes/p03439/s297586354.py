import sys

n=int(input())

left=0
right=n-1

print(left)
sl=input()
if sl=="Vacant":
  sys.exit()
print(right)
sr=input()
if sr=="Vacant":
  sys.exit()


sm=""
while right-left>=2:
  mid=(left+right)//2
  print(mid)
  sm=input()
  if sm=="Vacant":
    sys.exit()
  if (sl==sm and (mid-left)%2==0) or (sl!=sm and (mid-left)%2==1):
    left=mid
    sl=sm
  else:
    right=mid
    sr=sm

print(left)
if input()=="Vacant":
  sys.exit()
print(right)
if input()=="Vacant":
  sys.exit()
  
    
