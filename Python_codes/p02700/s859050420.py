a,b,c,d=map(int, input().split())

tk=c//b
ao=a//d
if c%b!=0:
  tk+=1
if a%d!=0:
  ao+=1

if tk>ao:
  print("No")
else:
  print("Yes")