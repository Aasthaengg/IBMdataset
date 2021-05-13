from collections import*
I=lambda:map(int,input().split())
n,m=I()
a=Counter(I())
for _ in[0]*m:b,c=I();a[c]+=b
s=0
for k,v in sorted(a.items())[::-1]:
 if n<v:exit(print(s+k*n))
 n-=v;s+=k*v