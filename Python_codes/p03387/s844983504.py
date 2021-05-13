z=list(map(int,input().split()))
list.sort(z, reverse=True)
c=z[0]
b=z[1]
a=z[2]
x=(c-b)//2 + (c-a)//2

if((c-b)%2==1):
  if((c-a)%2==1):
    x+=1
  else:
    x+=2
elif((c-a)%2==1):
  x+=2
print(x)