a,b,c,d=map(int,input().split())
n=a*b
m=c*d
p=[n,m]
p.sort()
print(p[1])