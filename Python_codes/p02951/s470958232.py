a,b,c=map(int,input().split())
if b+c<=a:
  print(str(0)+"\n")
else :
  print(str(c-(a-b))+"\n")