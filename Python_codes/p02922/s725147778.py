a,b=map(int,input().split())
if b==1: print(0); exit();
for i in range(1,1000):
  if b<=a*i-(i-1):
    print(i)
    exit(0)
