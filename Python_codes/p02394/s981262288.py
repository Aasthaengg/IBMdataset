import sys
prm = sys.stdin.readline()
prm = prm.split()
W = int(prm[0])
H = int(prm[1])
x = int(prm[2])
y = int(prm[3])
r = int(prm[4])

if r <= x and x <= (W-r) and r <= y and y <= (H-r) :
    print 'Yes'
else :
    print 'No'