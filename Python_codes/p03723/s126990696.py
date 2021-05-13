A,B,C=map(int,input().split())
ans=0
d=[]
a=A
b=B
c=C

while 1:
  if a%2!=0 or b%2!=0 or c%2!=0:
    print(ans)
    exit()
  if [a,b,c] in d:
    print(-1)
    exit()
  d.append([a,b,c])
  a1 = b//2 + c//2
  b1 = a//2 + c//2
  c1 = a//2 + b//2
  a=a1
  b=b1
  c=c1
  ans+=1