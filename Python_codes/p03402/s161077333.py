a,b=map(int,input().split())
h,w=100,100
c=[["."]*w if int(i)<50 else ["#"]*w for i in range(h)]

a-=1
b-=1
plus=True
h1,w1=0,0
while b:
  c[h1][w1]="#"
  b-=1
  if w1!=48:
    w1+=2
  else:
    if h1==48:break
    w1=0
    h1+=2
h2,w2=51,0
while a:
  c[h2][w2]="."
  a-=1
  if w2!=48:
    w2+=2
  else:
    if h2==99:break
    w2=0
    h2+=2
print(h,w)
for ci in c:
  ans=""
  for cc in ci:
    ans+=cc
  print(ans)

