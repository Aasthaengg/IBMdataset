_,*s=open(0);t='.';b=t*101;q=range(101)
for i,s in enumerate(s):
 a=[i]
 for x,y,z,c in zip(b,t+s,s,q):a+=min(c+(x==t>z),a[-1]+(y==t>z)),
 b,q=s,a[1:]
print(a[-2])