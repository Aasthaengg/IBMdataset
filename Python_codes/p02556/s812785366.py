from sys import stdin
nii=lambda:map(int,stdin.readline().split())
lnii=lambda:tuple(map(int,stdin.readline().split()))

n=int(input())

l=set(tuple([lnii() for i in range(n)]))

if len(l)==1:
  print(0)
  exit()

x_max=0
x_min=10**10
y_max=0
y_min=10**10

for x,y in l:
#  s=abs(x-y)
  s=x-y
  x_max=max(x_max,s)
  x_min=min(x_min,s)

#  t=abs(x+y)
  t=x+y
  y_max=max(y_max,t)
  y_min=min(y_min,t)

x_ans=x_max-x_min
y_ans=y_max-y_min
print(max(x_ans,y_ans))