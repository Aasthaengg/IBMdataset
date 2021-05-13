def main():
    import sys
    input = sys.stdin.readline
    from bisect import bisect_left

    N, Q = map(int, input().split())
    c = []
    c_append = c.append
    for _ in range(N):
        s, t, x = map(int, input().split())
        c_append((x, s, t))
    c.sort()

    D = [int(input()) for _ in range(Q)]

    ans = [-1] * Q
    skip = [-1] * Q

    for x, s, t in c:
        left = bisect_left(D, s - x)
        right = bisect_left(D, t - x)
        while left < right:
            if skip[left] == -1:
                ans[left] = x
                skip[left] = right
                left += 1
            else:
                left = skip[left]

    print ('\n'.join(map(str, ans)))

if __name__ == '__main__':
    main()