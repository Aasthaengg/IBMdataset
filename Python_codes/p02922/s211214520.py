import sys
a,b=list(map(int,input().split()))
if b==1:
  print(0)
  sys.exit()
for i in range(100):
  if a+(a-1)*i >=b:
    print(i+1)
    sys.exit()