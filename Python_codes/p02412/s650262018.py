while True:
    n,x = map(int,raw_input().split())
    if n==0 and x==0:
        break
    ct = 0
    for i in xrange(1, n+1):
       for j in xrange(i+1, n+1):
           for k in xrange(j+1, n+1):
               if (i+j+k) == x:
                   ct += 1
    print ct