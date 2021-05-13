def resolve():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    sortedA = sorted(A)
    for a in A:
        if a == sortedA[-1]:
            print(sortedA[-2])
        else:
            print(sortedA[-1])

    
if '__main__' == __name__:
    resolve()