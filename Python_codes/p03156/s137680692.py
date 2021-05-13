from sys import stdin
nii=lambda:map(int,stdin.readline().split())
lnii=lambda:list(map(int,stdin.readline().split()))

n=int(input())
a,b=nii()
p=lnii()

x=0
y=0
z=0

for i in p:
  if i<=a:
    x+=1
  elif i>=b+1:
    z+=1
  else:
    y+=1

print(min(x,y,z))