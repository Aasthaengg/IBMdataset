while True:
    h,w = map(int,raw_input().split())
    if h==0 and w==0:
        break
    sside=""
    for x in xrange(w):
        sside += "#"
    for x in xrange(h):
        print sside
    print