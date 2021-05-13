n=int(input())
a=list(map(int,input().split()))
b=sorted(a)
x=b[n//2-1]
y=b[n//2]
for i in a:
    if i<=x:
      print(y)
    else:
      print(x)
