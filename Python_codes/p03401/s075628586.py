n=int(input())
a=list(map(int,input().split()))
a=[0]+a+[0]
x=[abs(a[i]-a[i-1]) for i in range(1,n+2)]
s=sum(x)
for i in range(n):
  print(s if (a[i+2]-a[i+1])*(a[i+1]-a[i])>0 else s-x[i]-x[i+1]+abs(a[i+2]-a[i]))