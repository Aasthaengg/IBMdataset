n=int(input())
a=list(map(int,input().split()))
b=a[:]

x=0#pmpm
y=0
sum1=0
sum2=0

for i in range(n):
  sum1+=a[i]
  sum2+=b[i]
  if(i%2==0):
    if(sum1<=0):
      x+=1-sum1
      a[i]+=1-sum1
      sum1+=1-sum1
    if(sum2>=0):
      y+=sum2+1
      b[i]-=sum2+1
      sum2-=sum2+1
  else:
    if(sum1>=0):
      x+=sum1+1
      a[i]-=1+sum1
      sum1-=1+sum1
    if(sum2<=0):
      y+=1-sum2
      b[i]+=1-sum2
      sum2+=1-sum2
print(min(x,y))