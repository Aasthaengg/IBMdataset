import string
L = string.split(raw_input())
W = int(L[0])
H = int(L[1])
x = int(L[2])
y = int(L[3])
r = int(L[4])

if x - r < 0:
    print "No"
elif y - r < 0:
    print "No"
elif x + r > W:
    print "No"
elif y + r > H:
    print "No"
else:
    print "Yes"