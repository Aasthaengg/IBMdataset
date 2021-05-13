a,b,c=map(int,input().split())
cnt=0
while a%2==b%2==c%2==0:
  a1=a//2
  b1=b//2
  c1=c//2
  a=b1+c1
  b=c1+a1
  c=a1+b1
  cnt+=1
  if a==2*a1 and b==2*b1 and c==2*c1:
    cnt=-1
    break
print(cnt)