def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(k, n):
        if a[i] > a[i-k]:
            print('Yes')
        else:
            print('No')


if __name__ == '__main__':
    solve()
