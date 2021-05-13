from bisect import bisect

def solve():
    N = int(input())
    A = sorted(map(int,input().split()))
    if N == 2:
        res = [(max(A),min(A))]
        s = max(A)-min(A)
        return s, res

    if A[0] >= 0:
        res = []
        x = A[0]
        for a in A[1:-1]:
            res.append((x,a))
            x -= a
        res.append((A[-1],x))
        x = A[-1]-x
        return (x,res)
    if A[-1] <= 0:
        res = []
        x = A[-1]
        for a in A[:-1]:
            res.append((x,a))
            x -= a
        return (x,res)

    res = []
    p = bisect(A,0)-1
    x = A[p]
    for a in A[p+1:N-1]:
        res.append((x,a))
        x -= a
    res.append((A[-1],x))
    x = A[-1]-x
    for a in A[:p]:
        res.append((x,a))
        x -= a
    return (x,res)



s,res = solve()
print(s)
print('\n'.join(f'{a} {b}' for a,b in res))