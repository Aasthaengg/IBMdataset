cnt = 0


def insertionSort(arr, N, g):
    global cnt
    for i in range(g, N):
        tmp = arr[i]
        j = i - g
        while(j >= 0 and arr[j] > tmp):
            arr[j + g] = arr[j]
            j -= g
            cnt += 1
        arr[j + g] = tmp


def shellSort(arr, N):
    G = []
    h = 0
    m = 0
    while h <= N / 9:
        h = 3 * h + 1
        m += 1
        G.append(h)
    G = G[::-1]
    for g in G:
        insertionSort(arr, N, g)
    return G


N = int(input())
arr = [int(input()) for i in range(N)]

G = shellSort(arr, N)
print(len(G), ' '.join(map(str, G)), cnt, '\n'.join(map(str, arr)), end='\n')

