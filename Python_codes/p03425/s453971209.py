n=int(input())
s=[input() for _ in range(n)]
m=sum([1 for i in s if i[0]=='M'])
a=sum([1 for i in s if i[0]=='A'])
r=sum([1 for i in s if i[0]=='R'])
c=sum([1 for i in s if i[0]=='C'])
h=sum([1 for i in s if i[0]=='H'])
print(m*a*r+m*a*c+m*a*h+m*r*c+m*r*h+m*c*h+a*r*c+a*r*h+a*c*h+r*c*h)