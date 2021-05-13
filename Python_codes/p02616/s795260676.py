n,k,*a=map(int,open(0).read().split())
a.sort()
p=a.pop
s=b=~k%2or p()
i=0
for _ in k//2*'_':
 x=a[i]*a[i+1]
 if x*b>a[-1]*a[-2]*b:s*=x;i+=2
 else:s*=p()*p()
 s%=10**9+7
print(s)