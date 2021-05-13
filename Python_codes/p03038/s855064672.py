import bisect
def resolve():
    N, M = list(map(int, input().split()))
    A = sorted(list(map(int, input().split(" "))))
    BC = sorted([list(map(int, input().split())) for _ in range(M)], key=lambda x: x[1], reverse=True)
    ptr = 0
    total = 0
    for i in range(M):
        num, val = BC[i]
        _ptr = min(ptr+num, bisect.bisect_left(A, val))
        if _ptr > ptr:
            total += val*(_ptr-ptr)
            ptr = _ptr
    total += sum(A[ptr:])
    print(total)

if '__main__' == __name__:
    resolve()