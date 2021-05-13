def insertionSort(arr, g):
    cnt = 0
    for i in range(g, len(arr)):
        tmp = arr[i]
        j = i - g
        while(j >= 0 and arr[j] > tmp):
            arr[j + g] = arr[j]
            j -= g
            cnt += 1
        arr[j + g] = tmp
    return cnt


def shellSort(arr):
    cnt = 0
    g = []
    h = 0
    while h <= len(arr) / 9:
        h = 3 * h + 1
        g.append(h)
    g = g[::-1]
    m = len(g)

    for i in range(0, m):
        cnt += insertionSort(arr, g[i])
    return (cnt, g)


N = int(input())
arr = [int(input()) for i in range(N)]

(cnt, g) = shellSort(arr)
print(len(g))
print(' '.join(map(str, g)))
print(cnt)
print('\n'.join(map(str, arr)))

