a,b,c = map(int,input().split())
cou = 0
if  a%2==0 and a==b and b==c and c==a :
  print(-1)
  exit()
while a%2==0 and b%2==0 and c%2==0:
  j=int(a//2)
  k=int(b//2)
  m=int(c//2)
  a += k+m
  b += j+m
  c += j+k
  cou += 1
print(cou)