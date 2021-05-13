import sys
def insertionSort(A, n, g):
    global cnt
    for i in range(g, n):
        v = A[i]
        j = i - g
        while j >= 0 and A[j] > v:
            A[j + g] = A[j]
            j = j - g
            cnt += 1
        A[j + g] = v
def solve():
    n = int(input())
    A = list(map(int, sys.stdin))
    G = [int((2.25**i - 1) / 1.25)for i in range(17, 0, -1)]
    G = [v for v in G if v <= n]
    for g in G:
        insertionSort(A, n, g)
    print(len(G))
    print(*G)
    print(cnt)
    print('\n'.join(map(str, A)))
if __name__ == '__main__':
    cnt = 0
    solve()
