h,w=map(int,input().split())
s=''
for _ in range(h):
  s+=input()
from collections import Counter as c
v=list(c(s).values())
ki=0;ni=0;
for i in v:
  if i%2:
    ki+=1
  elif i%4:
    ni+=1
x='No'
if (h%2)*(w%2):
  if ki==1 and ni<=(h+w-2)//2:
    x='Yes'
elif h%2:
  if ki==0 and ni<=w//2:
    x='Yes'
elif w%2:
  if ki==0 and ni<=h//2:
    x='Yes'
else:
  if ki==0 and ni==0:
    x='Yes'
print(x)