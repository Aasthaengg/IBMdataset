n=int(input())
a=sorted(list(map(int,input().split())))
m=-a[0]
for i in a[1:-1]:
  if i<0:m-=i
  else:m+=i
m+=a[-1] 
print(m)
b,c=a[0],a[-1]
for i in a[1:-1]:
  if i>0:
    print(b,i)
    b-=i
  else:
    print(c,i)
    c-=i
print(c,b)