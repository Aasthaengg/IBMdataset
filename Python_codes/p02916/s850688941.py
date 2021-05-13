n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))
Sum=sum(b)
for i in range (0,len(a)-1):
  if a[i]+1==a[i+1]:
    number=a[i]
    Sum+=c[number-1]
print(Sum)