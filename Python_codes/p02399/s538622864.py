a,b=map(int, raw_input().split())
d=a/b
e=a%b
print "{0} {1} {2:0.8f}".format(int(d), int(e), float(a)/float(b))