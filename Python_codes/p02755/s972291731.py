a,b=map(int,input().split())
c=0
x=int(b/0.1)
for i in range(x,x+10):
  if int(i *0.08)==a:
    print(i)
    c=1
    break
if c==0:
  print(-1)

