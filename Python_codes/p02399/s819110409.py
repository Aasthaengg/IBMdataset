a,b = map(int,raw_input().split())

d=a // b
r=a % b
f=float(a) / b

print d,r,"{0:f}".format(f)