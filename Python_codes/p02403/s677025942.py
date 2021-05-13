import math

H, W = map(int, raw_input().split())

while H > 0 or W > 0 :
    for i in xrange(H) :
        print "#" * W

    print 

    H, W = map(int, raw_input().split())