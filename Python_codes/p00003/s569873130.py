import sys
n = raw_input()
for line in sys.stdin:
    li = sorted([int(x) for x in line.split()],reverse=True)
    print "YES" if (li[0]**2 == li[1]**2 + li[2]**2) else "NO"