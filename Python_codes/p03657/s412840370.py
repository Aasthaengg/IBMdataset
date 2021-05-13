A, B = map(int, raw_input().split())
if (A + B) % 3 == 0:
    print "Possible"
elif A % 3 == 0 or B % 3 == 0:
    print "Possible"
else:
    print "Impossible"
