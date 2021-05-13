import sys
while True:
    ls = map(int, raw_input().split())
    if ls[0]==0 and ls[1]==0:
        break
    for h in xrange(ls[0]):
        for w in xrange(ls[1]):
            #print '#',
            sys.stdout.write('#')
        print ''
    print ''