a,b,c,d=input().split()
a=int(a)
b=int(b)
c=int(c)
d=int(d)
p=a*c
q=a*d
r=b*c
s=b*d
print(max(p,q,r,s))