rr = raw_input
rrm = lambda: map(int, rr().split())

N, K = rrm()

N -= K
if K == 1:
    print 0
else:
    print N
    
