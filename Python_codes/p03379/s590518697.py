n=int(input())
x=list(map(int,input().split()))
l=sorted(x)
a,b=l[n//2-1],l[n//2]
for i in x:
 if (a+b)/2<=i:print(a)
 else:print(b)