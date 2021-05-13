def resolve():
    N = int(input())
    A = sorted(list(map(int, input().split())))
    n = A[-1]
    import bisect
    idx = bisect.bisect_left(A, n//2)
    candidates = []
    if idx < N:
        candidates.append(A[idx])
    if idx > 0:
        candidates.append(A[idx-1])

    if abs(n/2 - candidates[0]) < abs(n/2 - candidates[1]):
        print(n, candidates[0])
    else:
        print(n, candidates[1])       

    
if '__main__' == __name__:
    resolve()