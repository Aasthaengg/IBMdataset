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

if len(A)!=2**(m+1):
    print -1
    sys.exit()

xorsum = [0]
for a in A:
    xorsum.append(xorsum[-1]^a)

index = [-1]*(2**m)
for i in range(len(A)):
    if index[A[i]] == -1:
        index[A[i]] = i
    else:
        j = index[A[i]]
        if (xorsum[i+1]^xorsum[j])!=k:
            print -1
            sys.exit()

print ' '.join(str(a) for a in A)