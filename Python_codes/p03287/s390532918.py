import sys
import math

def resolve():
    N, M = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = [0]
    cur = 0
    for a in A:
        cur += a
        B.append(cur)
    #print(B)
    C = []
    for b in B:
        C.append(b%M)
    import collections
    counts = collections.Counter(C)
    #print(counts)
    ans = 0
    for count in counts.values():
        ans += count*(count-1)//2
    print(ans)

if '__main__' == __name__:
    resolve()