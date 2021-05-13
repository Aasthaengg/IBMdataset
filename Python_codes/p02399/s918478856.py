from decimal import Decimal
a,b = map(int,raw_input().split())

d=a/b
r=a%b

print "%d %d %f" %(d,r,float(a)/b)