from collections import*
n,*v=map(int,open(0).read().split())
a,b=[Counter(v[i::2]).most_common()+[(0,0)]for i in(0,1)]
s,x=a[0]
t,y=b[0]
print(n-[x+y,max(x+b[1][1],y+a[1][1])][s==t])