n,k,*a=map(int,open(0).read().split())
a.sort()
p=a.pop
s=b=~k%2or p()
i=0
while k>1:
 x=a[i]*a[i+1]
 if x*b>a[-1]*a[-2]*b:i+=2
 else:x=p()*p()
 s=s*x%(10**9+7);k-=2
print(s)