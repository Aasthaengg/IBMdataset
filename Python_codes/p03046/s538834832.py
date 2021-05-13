import sys
range = xrange
input = raw_input

m,k = [int(x) for x in input().split()]

if (m==1 and k==1) or k>=2**m:
    print -1
    sys.exit()

if k==0:
    A = list(range(2**m))
    print ' '.join(str(a) for a in (A + A[::-1]))
    sys.exit()

A = [i for i in range(2**m) if i != k]

A = A + [k] + A[::-1] + [k]

print ' '.join(str(a) for a in A)
