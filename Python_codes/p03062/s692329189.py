n=int(input())
a=list(map(int,input().split()))
sm=sum(map(abs,a))
f=1

for i in range(n-1):
  f= 1 if a[i]*f>=0 else -1
print (sm if f*a[n-1]>0  or 0 in a else sm-2*min(map(abs,a)))