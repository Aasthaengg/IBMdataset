def resolve():
    N = int(input())
    A = list(map(int, input().split()))
    maximum, minimum = max(A), min(A)
    maxidx = A.index(maximum)
    minidx = A.index(minimum)
    ops = []

    for i in range(N):
        if abs(maximum) > abs(minimum):
            A[i] += maximum
            ops.append((maxidx, i))
        else:
            A[i] += minimum
            ops.append((minidx, i))
    
    #print(A)

    if abs(maximum) > abs(minimum):
        for i in range(0, N-1):
            ops.append((i, i+1))
            A[i+1] += A[i]
    else:
        for i in range(N-1, 0, -1):
            ops.append((i, i-1))
    
    #print(A)
    print(len(ops))
    [print(v[0]+1, v[1]+1) for v in ops]
    

if '__main__' == __name__:
    resolve()