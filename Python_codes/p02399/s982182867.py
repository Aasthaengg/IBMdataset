import fpformat
a,b= map(int,raw_input().split())
d = a/b
r = a%b
f = a/float(b)
print d,r,fpformat.fix(f, 8)