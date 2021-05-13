x,y=a,b=map(int,raw_input().split())
while True:
  if x%y==0:break
  x,y=(y,x%y)
print "%d" % y