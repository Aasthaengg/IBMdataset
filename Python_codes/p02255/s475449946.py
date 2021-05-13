import sys
import math

n = input()
a = map(int, raw_input().split())

for i in xrange(n) :
    tmp = a[i]
    a.pop(i)

    for j in xrange(i) :
        if a[j] > tmp :
            a.insert(j, tmp)
            break
    else :
        a.insert(i, tmp)

    for j in xrange(n) :
        sys.stdout.write(str(a[j]))
        if j < n-1 :
            sys.stdout.write(" ")

    print