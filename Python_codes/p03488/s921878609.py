s=input()
x,y=map(int,input().split())
t=s.split("T")
x-=len(t[0])
dx,dy=[],[]

for i,tt in enumerate(t[1:]):
  if i%2==1:
    dx.append(len(tt))
  else:
    dy.append(len(tt))

def is_ok(n,l):
  dp=set([0])
  for d in l:
    t=[]
    for v in dp:
      t.append(v+d)
      t.append(v-d)
    dp=set(t)
  return True if n in dp else False

if is_ok(x,dx) and is_ok(y,dy):
  print("Yes")
else:
  print("No")

