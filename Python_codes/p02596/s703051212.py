k=int(input())
if k&1==0 or k%5==0:
  print(-1)
  exit()
elif 7%k==0:
  print(1)
  exit()
m=7
a=b=1
while(m>0):
  a=a*10%k
  m=(m+7*a)%k
  b+=1
print(b)