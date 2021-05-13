if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    n = int(input())
    color_dict = {}
    ans = 1
    front_c = 0
    for _ in range(n):
        c = input().rstrip()
        if c != front_c:
            try:
                ans += color_dict[c]
                color_dict[c] = ans
            except KeyError:
                color_dict[c] = ans
            front_c = c
    print(ans%(10**9+7))
