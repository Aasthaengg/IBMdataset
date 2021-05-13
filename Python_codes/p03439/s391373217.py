def main():
    import sys
    input = sys.stdin.readline
    N = int(input())
    print(0, flush=True)
    s = input().strip()
    if s == 'Vacant':
        return True
    ls, rs = s, s
    l, r = 0, N
    while True:
        m = (l + r) // 2
        print(m, flush=True)
        s = input().strip()
        if s == 'Vacant':
            return True
        if (m - l) % 2 == 0 and s != ls:
            r = m
            rs = s
        elif (m - l) % 2 == 1 and s == ls:
            r = m
            rs = s
        elif (r - m) % 2 == 0 and s != rs:
            l = m
            ls = s
        elif (r - m) % 2 == 1 and s == rs:
            l = m
            ls = s

if __name__ == '__main__':
    main()