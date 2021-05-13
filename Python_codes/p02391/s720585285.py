import sys
prm = sys.stdin.readline()
prm = prm.split()
a = int(prm[0])
b = int(prm[1])
if a > b :
    print 'a > b'
elif a < b :
    print 'a < b'
else:
    print 'a == b'