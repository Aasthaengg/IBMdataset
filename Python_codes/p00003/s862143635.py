for i in range(int(raw_input())):
    sides = map(int, raw_input().split())
    if sides[0]**2 == sides[1]**2 + sides[2]**2 or\
       sides[1]**2 == sides[2]**2 + sides[0]**2 or\
       sides[2]**2 == sides[0]**2 + sides[1]**2:
           print "YES"
    else:
        print "NO"