s=int(input())
x1,y1=0,0
x2,y2=10**9,1
x3,y3=0,0

mod=10**9
r=(mod-s%mod)%mod
q=(s+r)/mod
x3=int(r)
y3=int(q)
print(x1,y1,x2,y2,x3,y3)
