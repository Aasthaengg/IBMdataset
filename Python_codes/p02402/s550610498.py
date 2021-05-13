import sys
 
l = [map(int,line.split()) for line in sys.stdin]
n = l[0]
l = l[1]
 
print "%s %s %s" %(min(l),max(l),sum(l))