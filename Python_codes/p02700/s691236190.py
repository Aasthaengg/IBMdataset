a,b,c,d=input().split()
a=int(a)
b=int(b)
c=int(c)
d=int(d)
e=0
while e==0:
  c=c-b
  if c<=0:
    print("Yes")
    break
  a=a-d
  if a<=0:
    print("No")
    break