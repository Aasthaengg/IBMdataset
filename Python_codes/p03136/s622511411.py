def solve():
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    if sum(l[:n-1]) > l[n-1]:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    solve()
