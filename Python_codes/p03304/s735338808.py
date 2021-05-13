def main():
    import sys
    import decimal
    input = sys.stdin.readline
    n, m, d = [int(x) for x in input().strip().split()]
    if d == 0:
        print((m-1)/n)
        return True
    print(((n-d)*2*(m-1) / pow(n, 2)))

if __name__ == '__main__':
    main()