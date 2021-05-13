a,b,c=map(int,input().split())
for i in [a,b,c]:
  if i%2==0:
    print(0)
    break
else:
  s=min(a*b,b*c,c*a)
  print(int(s))