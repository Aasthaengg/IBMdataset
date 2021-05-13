_,*s=open(0);t="."
b=t*101;q=range(101);i=0
for s in s:
 a=[i];i+=1
 for x,y,z,c in zip(b,t+s,s,q):a+=min(c+(t>z<x),a[-1]+(t>z<y)),
 b,q=s,a[1:]
print(a[-2])