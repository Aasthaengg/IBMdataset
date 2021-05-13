import math
while True:
  n=int(input())
  if n==0:
    break
  s=list(map(int,input().split()))
  m=sum(s)/len(s)
  bunsan2=0
  for i in range(n):
    bunsan2+=(s[i]-m)**2
  bunsan=bunsan2/n
  hensa=math.sqrt(bunsan)
  print(f"{hensa:.8f}")
