import itertools
def main():
    n, m = list(map(int, input().split()))
    A = [[] for _ in range(n)]
    for i in range(m):
        p, y = list(map(int, input().split()))
        A[p - 1].append([i, y])
    for i, a in enumerate(A):
        a.sort(key = lambda x: x[1])
        for j in range(len(a)):
            a[j] = [a[j][0], '{:06}{:06}'.format(i + 1, j + 1)]
    A = list(itertools.chain.from_iterable(A))
    A.sort(key = lambda x: x[0])
    for a in A:
        print(a[1])

if __name__ == '__main__':
    main()
