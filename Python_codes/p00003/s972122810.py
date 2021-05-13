n = input()
for x in xrange(n):
    sides = map(int,raw_input().split())
    sides = sorted(sides)
    if sides[0]**2+sides[1]**2==sides[2]**2:
        print "YES"
    else:
        print "NO"