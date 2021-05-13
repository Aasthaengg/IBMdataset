h=int(input())
w=int(input())
n=int(input())         
if h>w:
  if n%h==0:
    ct=n//h
  else:
    ct=n//h+1
else:
  if n%w==0:
    ct=n//w
  else:
    ct=n//w+1
print(ct)