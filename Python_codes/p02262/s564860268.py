import sys

def insertionSort(A,N,g):
    cnt = 0
    for i in range(g,len(A)):
        v = A[i]
        j = i - g
       
        while j >= 0 and A[j] > v:
            A[j+g] = A[j]
            j -= g
            cnt += 1
        A[j+g] = v
    return cnt


def shellSort(A,N):
    cnt = 0
    G = [(3**i-1)//2 for i in range(1,17) if ((3**i-1)//2) <= N]
    m = len(G)
    for i in reversed(range(m)):
        cnt += insertionSort(A,N,G[i])

    print(len(G))
    print(" ".join(map(str,reversed(G))))
    print(cnt)
    print("\n".join(map(str,A)))


N = int(input())
#lst = list(map(int, [input() for i in range(N)]))
lst = [int(l) for l in sys.stdin.readlines()]
#lst = [i for i in range(100000)]
#reversed(lst)
shellSort(lst,N)

