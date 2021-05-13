cnt = 0

def insertionSort(A, n, g):
    global cnt
    for i in range(g, n):
        v = A[i]
        j = i-g
        while j >= 0 and A[j] > v:
            A[j+g] = A[j]
            j -= g
            cnt += 1
        A[j+g] = v


def shellSort(A, n):
    G = [1]
    while G[-1]*3+1 < n:
        G.append(G[-1]*3 + 1)

    for i in range(len(G)-1, -1, -1):
        insertionSort(A, n, G[i])

    G.reverse()

    print len(G)
    print " ".join(map(str, G))
    print cnt


N = int(raw_input())
L = [int(raw_input()) for i in range(N)]

shellSort(L, N)


for i in L:
    print i