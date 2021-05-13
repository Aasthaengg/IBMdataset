a,b,c=map(int,input().split())
d=0
while d<10:
  c=a*c-b
  print(c)
  d+=1
