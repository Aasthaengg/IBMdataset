def main():
    import sys
    read = sys.stdin.buffer.read
    readline = sys.stdin.buffer.readline
    readlines = sys.stdin.buffer.readlines
    sys.setrecursionlimit(10 ** 7)
    
    from itertools import accumulate

    n, k = map(int, readline().split())
    a = list(map(int, readline().split()))
    check = [n] * n
    for i in range(k):
        memo = [0] * (n + 1)
        for j, aa in enumerate(a):
            memo[max(0, j - aa)] += 1
            memo[min(n, j + aa + 1)] -= 1
        a = list(accumulate(memo))[:-1]
        if a == check:
            break
    print(*a)


if __name__ == '__main__':
    main()
