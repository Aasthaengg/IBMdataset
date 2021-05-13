n,a,b=map(int,input().split())
x=b-a
p=print
if (b-a)%2==0:p((b-a)//2)
else:p(min(n-b+1+(x-1)//2,a+x//2))