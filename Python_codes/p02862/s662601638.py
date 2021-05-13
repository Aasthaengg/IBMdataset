inp=list(map(int,input().split()))
x=inp[0]
y=inp[1]
if (x+y)%3!=0:
  print (0)
else:
  flag=0
  z=(x+y)//3
  n=x-z
  m=y-z
  if m<0 or n<0:
    print (0)
    flag=1
  else:
    arr=[1]
    v=pow(10,9)+7
    for i in range(1,m+n+1):
      arr.append((arr[-1]*i)%v)
    a=arr[m+n]
    b=(arr[m]*arr[n])%v
    print ((a*pow(b,v-2,v))%v)