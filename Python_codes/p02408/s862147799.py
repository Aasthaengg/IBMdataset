import sys
n = input()
count = 0
Ss = []
Hs = []
Cs = []
Ds = []
while count<n:
    mark, num = raw_input().split()
    #num = int(num)
    if mark == 'S':
        Ss.append(num)
    elif mark == 'H':
        Hs.append(num)
    elif mark == 'C':
        Cs.append(num)
    elif mark == 'D':
        Ds.append(num)
    else :
        print "error"
        sys.exit()
    count+=1
for x in xrange(1,14):
    if str(x) not in Ss:
        print "S "+str(x)
for x in xrange(1,14):
    if str(x) not in Hs:
        print "H "+str(x)
for x in xrange(1,14):
    if str(x) not in Cs:
        print "C "+str(x)
for x in xrange(1,14):
    if str(x) not in Ds:
        print "D "+str(x)