while True:
    try:
        (h,w)=map(int,raw_input().split())
        if h==0 and w==0: break
        for i in xrange(h):
            if i==0 or i==h-1:
                print ''.join(['#' for j in xrange(w)])
            else:
                print '#'+(''.join(['.' for j in xrange(w-2)]))+"#"
        print
    except EOFError: break