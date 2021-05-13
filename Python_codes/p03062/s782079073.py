n=int(input())
a=list(map(int,input().split()))
b=[abs(i) for i in a]

minus=0
for i in a:
  if i<0:
    minus+=1
    
if minus%2==1:
  print(sum(b)-min(b)*2)
else:
  print(sum(b))