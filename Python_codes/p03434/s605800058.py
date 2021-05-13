a=int(input())
b=[int(i) for  i in input().split()]
c=sorted(b,reverse=True)
x=0
y=0
for j in range(len(c)):
  if j%2==0:
    x+=c[j]
  else:
    y+=c[j]
print(x-y)