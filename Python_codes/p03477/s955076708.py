A, B, C, D = map(int, raw_input() .split())
if A + B > C + D:
    print "Left"
elif C + D > A + B:
    print "Right"
elif A + B == C + D:
    print "Balanced"
