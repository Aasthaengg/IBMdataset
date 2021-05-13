n = input()
A = [input() for i in range(n)]

def insertionSort(A,n,g):
    cnt = 0
    for i in range(g,n):
        v = A[i]
        j = i - g
        while j >= 0 and A[j] > v:
            A[j+g] = A[j]
            j -= g
            cnt += 1
        A[j+g] = v

    return cnt

def shellSort(A,n):
    cnt = 0
    m = int((n-1)/3)
    G = [1]
    for i in range(1,n):
        gn = G[i-1]+3**i
        if gn > n:
            break
        G.append(gn)
    m = len(G)
    for i in range(m):
        j = (m-1) - i
        cnt += insertionSort(A,n,G[j])

    return m, G, cnt

m, G, cnt = shellSort(A,n)

print m

for i in range(1,m):
    j = m - i
    print G[j],
print G[0]

print cnt

for item in A:
    print item