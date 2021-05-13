def insertionSort(A, N, g):
    global cnt
    for i in range(g, N):
        v = A[i]
        j = i - g
        while j >= 0 and A[j] > v:
            A[j + g] = A[j]
            j -= g
            cnt += 1
        A[j + g] = v

def shellSort(A, N):
    global cnt
    cnt = 0

    G = []
    g = 1
    while g <= N:
        G.insert(0, g)
        g = 3 * g + 1

    for g in G:
        insertionSort(A, N, g)

    print len(G)
    print " ".join(str(g) for g in G)
    print cnt
    for i in A:
        print i

if __name__ == "__main__":
    N = input()
    A = []
    for i in range(N):
        A.append(input())
    shellSort(A, N)