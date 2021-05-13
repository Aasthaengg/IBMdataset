def insertionSort(A, n, g):
    cnt = 0
    for i in xrange(g, n, 1):
        v = A[i]
        j = i - g
        while j >= 0 and A[j] > v:
            A[j+g] = A[j]
            j = j - g
            cnt += 1
        A[j+g] = v
    return cnt

def shellSort(A, n):
    cnt = 0
    G = [1]
    i = 0
    while G[i] * 3 + 1 <= n:
        G.append(G[i] * 3 + 1)
        i += 1
    G.reverse()
    m = len(G)
    print m
    print ' '.join(map(str, G))
    for x in G:
        cnt += insertionSort(A, n, x)
    return cnt

N = int(raw_input())
A = [int(raw_input()) for i in xrange(N)]
cnt = shellSort(A, N)
print cnt
for i in A:
    print i