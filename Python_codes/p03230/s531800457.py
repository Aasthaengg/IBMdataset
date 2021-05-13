def main():
    N = int(input())
    # N=1: {1}, {1} (1*2)
    # N=3: {1, 2}, {1, 3}, {2, 3} (2*3)
    # N=6: {1, 2, 3}, {1, 4, 5}, {2, 4, 6}, {3, 5, 6} (3*4)
    # N=10:{1, 2, 3, 4}, {1, 5, 6, 7}, {2, 5, 8, 9}, {3, 6, 9, 10}, {4, 7, 8, 10} (4*5)
    # N=n(n+1)/2のケース(n=1,2,...)で構成可能
    # 集合の数はn+1で要素数はn
    n = 1
    while n * (n + 1) < 2 * N:
        n += 1
    if n * (n + 1) != 2 * N:
        print('No')
        return
    ans = [list() for _ in range(n + 1)]
    num = 0
    for left in range(n):
        for right in range(left + 1, n + 1):
            num += 1
            ans[left].append(num)
            ans[right].append(num)
    print('Yes')
    print(len(ans))
    for li in ans:
        print('{} {}'.format(len(li), ' '.join(map(str, li))))


if __name__ == '__main__':
    main()
