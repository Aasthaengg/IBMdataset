import sys                                                                                                                                                                                                                                                                                      
def range_union(al,ah,bl,bh):
    cl = max(al,bl)
    ch = min(ah,bh)
    if cl > ch:
        return 0
    else:
        return ch-cl +1
 
N = int(sys.stdin.readline())
T = map(int,sys.stdin.readline().strip().split())
A = map(int,sys.stdin.readline().strip().split())
 
p = 1
if N >= 2:
    Tl = T[0]
    Th = T[0]
    if A[0] > A[1]:
        Al = A[0]
        Ah = A[0]
    elif A[1] == A[0]:
        Al = 1
        Ah = A[0]
    else:
        p = 0
        print p
        exit(0)
 
    r = range_union(Tl,Th,Al,Ah)
    if not r:
        p = 0
        print p
        exit(0)
    else:
        p = (p*r) % 1000000007
        
for i in xrange(1,N-1):
    if T[i-1] < T[i]:
        Tl = T[i]
        Th = T[i]
    elif T[i-1] == T[i]:
        Tl = 1
        Th = T[i]
    else:
        p = 0
        break
        
    if A[i] > A[i+1]:
        Al = A[i]
        Ah = A[i]
    elif A[i+1] == A[i]:
        Al = 1
        Ah = A[i]
    else:
        p = 0
        break
 
    r = range_union(Tl,Th,Al,Ah)
    if not r:
        p = 0
        break
    else:
        p = (p*r) % 1000000007
 
if N >= 2:
    Al = A[-1]
    Ah = A[-1]
    if T[-1] > T[-2]:
        Tl = T[-1]
        Th = T[-1]
    elif T[-1] == T[-2]:
        Tl = 1
        Th = T[-1]
    else:
        p = 0
        print p
        exit(0)
 
    r = range_union(Tl,Th,Al,Ah)
    if not r:
        p = 0
        print p
        exit(0)
    else:
        p = (p*r) % 1000000007
 
if A[0] != T[-1]:
    print 0
    exit(0)
print p 