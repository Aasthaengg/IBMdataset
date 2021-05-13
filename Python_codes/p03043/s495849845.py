a,b=map(int,input().split())
r = 0
for i in range(1,a+1):
  tmp=1/a
  now=i
  while(now<b):
    now*=2
    tmp/=2
    #print(now, b)
  r+=tmp;
print(r)